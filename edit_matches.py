import sqlite3

DB_PATH = 'mtg-tournaments.db'

def connect_db(db_path=DB_PATH):
    """ Connect to the SQLite database. """
    return sqlite3.connect(db_path)

def view_decks(conn):
    """ View all decks in the Decks table. """
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Decks")
    decks = cursor.fetchall()
    print("\nDecks:")
    for deck in decks:
        print(f"ID: {deck[0]}, Name: {deck[1]}")
    print()

def view_matches(conn):
    """ View all matches in the Matches table. """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Matches")
    matches = cursor.fetchall()
    print("\nMatches:")
    for match in matches:
        print(match)
    print()

def update_deck_name(conn, old_name, new_name):
    """ Update the name of a deck in the Decks table. """
    cursor = conn.cursor()
    cursor.execute("UPDATE Decks SET name = ? WHERE name = ?", (new_name, old_name))
    conn.commit()
    print(f"Updated deck name from '{old_name}' to '{new_name}'.")

def update_match_result(conn, match_id, new_result):
    """ Update the result of a match in the Matches table. """
    cursor = conn.cursor()
    cursor.execute("UPDATE Matches SET result = ? WHERE id = ?", (new_result, match_id))
    conn.commit()
    print(f"Updated match ID {match_id} with new result: '{new_result}'.")

def main():
    conn = connect_db()
    
    while True:
        print("\nOptions:")
        print("1. View all decks")
        print("2. View all matches")
        print("3. Update deck name")
        print("4. Update match result")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_decks(conn)
        
        elif choice == '2':
            view_matches(conn)
        
        elif choice == '3':
            old_name = input("Enter the current deck name: ")
            new_name = input("Enter the new deck name: ")
            update_deck_name(conn, old_name, new_name)
        
        elif choice == '4':
            match_id = int(input("Enter match ID to update: "))
            new_result = input("Enter new match result (e.g., '2-1', '1-2'): ")
            update_match_result(conn, match_id, new_result)
        
        elif choice == '5':
            print("Exiting.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

    conn.close()

if __name__ == "__main__":
    main()
