import sqlite3

def connect_db(db_path='mtg-tournaments.db'):
    """ Connect to the SQLite database. """
    conn = sqlite3.connect(db_path)
    return conn

def insert_match(conn, player_deck_id, opponent_deck_id, tournament_date, tournament_location, result, opponent_name=None):
    """ Insert a match into the Matches table. """
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO Matches (player_deck_id, opponent_deck_id, location, date, result, opponent_name)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (player_deck_id, opponent_deck_id, tournament_location, tournament_date, result, opponent_name))
    
    conn.commit()
    print("Match inserted successfully.")

def get_deck_id(conn, deck_name):
    """ Get the Deck ID from the Decks table, inserting if it doesn't exist. """
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM Decks WHERE name = ?', (deck_name,))
    result = cursor.fetchone()
    
    if result:
        return result[0]  # Return existing deck ID
    else:
        cursor.execute('INSERT INTO Decks (name) VALUES (?)', (deck_name,))
        conn.commit()
        return cursor.lastrowid  # Return newly created deck ID

def get_user_input(match_num):
    """ Gather user input for a match. """
    print(f"\nEntering details for match {match_num + 1}:")
    
    opponent_deck = input("Enter opponent's deck name: ")
    result = input("Enter match result (e.g., 2-1, 1-2): ")
    opponent_name = input("Enter opponent's name (Press Enter if unknown): ")
    
    return (opponent_deck, result, opponent_name)

def main():
    conn = connect_db()
    
    # Ask for player's deck name once for the tournament
    player_deck = input("Enter your deck name: ")
    player_deck_id = get_deck_id(conn, player_deck)
    
    # Ask for tournament date and location
    tournament_date = input("Enter tournament date (YYYY-MM-DD): ")
    tournament_location = input("Enter tournament location: ")
    
    game_count = int(input("Enter the number of games: "))
    
    for match_num in range(game_count):
        user_input = get_user_input(match_num)
        opponent_deck_id = get_deck_id(conn, user_input[0])  # Get opponent's deck ID
        
        insert_match(conn, player_deck_id, opponent_deck_id, tournament_date, tournament_location, user_input[1], user_input[2])
    
    conn.close()

if __name__ == "__main__":
    main()
