import sqlite3

def connect_db(db_path='mtg-tournaments.db'):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_path)
    return conn

def fetch_stats(conn):
    """Fetch statistics from the database."""
    cursor = conn.cursor()
    
    # Total Matches
    cursor.execute('SELECT COUNT(*) FROM Matches')
    total_matches = cursor.fetchone()[0]

    # Decks Played
    cursor.execute('''
        SELECT d.name, COUNT(*) as match_count 
        FROM Matches m 
        JOIN Decks d ON m.player_deck_id = d.id 
        GROUP BY d.name
    ''')
    decks_played = cursor.fetchall()

    # Decks Played Against and Win Rates
    cursor.execute('''
        SELECT d.name, 
               COUNT(*) as match_count, 
               SUM(CASE 
                   WHEN result LIKE '2-%' THEN 1 
                   ELSE 0 
               END) as wins 
        FROM Matches m 
        JOIN Decks d ON m.opponent_deck_id = d.id 
        GROUP BY d.name
    ''')
    decks_played_against = cursor.fetchall()

    return total_matches, decks_played, decks_played_against

def update_readme(total_matches, decks_played, decks_played_against):
    """Update the README file with statistics."""
    readme_path = 'README.md'

    # Clear the README file first
    with open(readme_path, 'w') as file:
        file.write("# MTG-Tournament-Stats\n\n## Stats Overview\n")

    with open(readme_path, 'a') as file:
        file.write(f"- Total matches played: {total_matches}\n")
        file.write("- Decks I played:\n")
        
        for deck_name, match_count in decks_played:
            file.write(f"  - {deck_name}: {match_count} matches\n")

        file.write("- Decks I played against (win rate):\n")
        
        for opponent_deck_name, match_count, wins in decks_played_against:
            win_rate = (wins / match_count * 100) if match_count > 0 else 0
            file.write(f"  - {opponent_deck_name}: {match_count} matches, Win Rate: {win_rate:.2f}%\n")

def main():
    conn = connect_db()
    total_matches, decks_played, decks_played_against = fetch_stats(conn)
    update_readme(total_matches, decks_played, decks_played_against)
    conn.close()
    print("README.md updated with the latest stats.")

if __name__ == "__main__":
    main()
