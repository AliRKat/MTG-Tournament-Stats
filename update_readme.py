import sqlite3

def connect_db(db_path='mtg-tournaments.db'):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_path)
    return conn

def fetch_stats(conn):
    """Fetch general statistics and deck-opponent match stats from the database."""
    cursor = conn.cursor()
    
    # General stats
    cursor.execute('SELECT COUNT(*) FROM Matches')
    total_matches = cursor.fetchone()[0]
    
    cursor.execute('''
        SELECT SUM(CASE WHEN result LIKE '2-%' THEN 1 ELSE 0 END) AS matches_won,
               SUM(CAST(SUBSTR(result, 1, 1) AS INTEGER)) AS total_games_won,
               SUM(CAST(SUBSTR(result, 3, 1) AS INTEGER)) AS total_games_lost
        FROM Matches
    ''')
    matches_won, total_games_won, total_games_lost = cursor.fetchone()
    matches_lost = total_matches - matches_won

    # Decks Played with opponent match counts and win rates
    cursor.execute('''
        SELECT d.name AS player_deck_name, o.name AS opponent_deck_name,
               COUNT(*) AS match_count,
               SUM(CASE WHEN m.result LIKE '2-%' THEN 1 ELSE 0 END) AS wins
        FROM Matches m
        JOIN Decks d ON m.player_deck_id = d.id
        JOIN Decks o ON m.opponent_deck_id = o.id
        GROUP BY d.name, o.name
    ''')
    matches_by_deck = cursor.fetchall()

    return (total_matches, matches_won, matches_lost, total_games_won, total_games_lost, matches_by_deck)

def read_header(header_path='READMEHEADER.txt'):
    """Read the header text from a file."""
    with open(header_path, 'r') as file:
        return file.read()

def update_readme(header_text, stats):
    """Update the README file with statistics."""
    (total_matches, matches_won, matches_lost, total_games_won, total_games_lost, matches_by_deck) = stats
    
    readme_path = 'README.md'
    with open(readme_path, 'w') as file:
        file.write("# MTG-Tournament-Stats\n\n")
        file.write(header_text + "\n\n## Stats Overview\n")
        file.write(f"- Total matches played: {total_matches}\n")
        file.write(f"- Matches won: {matches_won}\n")
        file.write(f"- Matches lost: {matches_lost}\n")
        file.write(f"- Total games won: {total_games_won}\n")
        file.write(f"- Total games lost: {total_games_lost}\n\n")
        
        current_deck = None
        for player_deck_name, opponent_deck_name, match_count, wins in matches_by_deck:
            # Start a new section when the player's deck changes
            if player_deck_name != current_deck:
                if current_deck is not None:
                    file.write("\n")  # Add spacing between different player decks
                file.write(f"### Deck: {player_deck_name}\n")
                current_deck = player_deck_name
            
            # Calculate win rate
            win_rate = (wins / match_count * 100) if match_count > 0 else 0
            file.write(f"  - Opponent: {opponent_deck_name}, Matches: {match_count}, Win Rate: {win_rate:.2f}%\n")

def main():
    conn = connect_db()
    stats = fetch_stats(conn)
    header_text = read_header()
    update_readme(header_text, stats)
    conn.close()
    print("README.md updated with the latest stats.")

if __name__ == "__main__":
    main()
