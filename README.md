# MTG-Tournament-Stats

Welcome to the MTG Tournament Stats tool! This program helps me to track my performance in Magic: The Gathering tournaments by storing match results and generating statistics.


## Installation

```bash
git clone https://github.com/AliRKat/MTG-Tournament-Stats
cd MTG-Tournament-Stats
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
    
## Usage/Examples
To add a new tournament to the database, run the `insert_tournament.py` script. This will prompt you to input details such as the tournament name, deck used, opponent decks, and match results.
```bash
python insert_tournament.py
```
This script will guide you through entering:
- Tournament name and date
- Your deck and opponent decks
- Match results (e.g., "2-1" or "1-2")

Once you've added or edited matches in the database, you can update the README.md file to reflect the latest stats. The update_readme.py script will pull data from the database and rewrite the README with updated statistics.

```bash
python update_readme.py
```

If you need to make corrections or update the details of a match, use the edit_match.py script. This script allows you to:
- Locate a match by tournament or opponent name
- Update match results or deck information
- Save the updated details to the database

```bash
python edit_match.py
```


## Features

- Track matches and tournaments with detailed stats.
- Easy-to-use command-line interface.
- Automatically calculate win rates against different decks.


## DB Structure
- This tool uses SQLite for data storage, maintaining the following tables:
    - Decks: Records all decks played.
    - Matches: Stores match results, including player and opponent details.

## Contributing

Contributions are always welcome!

Feel free to fork the repository and submit pull requests for improvements or additional features.


## Stats Overview
- Total matches played: 11
- Matches won: 4
- Matches lost: 7
- Total games won: 13
- Total games lost: 17

### Deck: Mono Blue Tron
  - Opponent: Amulet Titan, Matches: 1, Win Rate: 100.00%
  - Opponent: Boros Energy, Matches: 1, Win Rate: 0.00%
  - Opponent: Domain Zoo, Matches: 1, Win Rate: 0.00%
  - Opponent: RG Breach/Eldrazi, Matches: 1, Win Rate: 100.00%
  - Opponent: UB Murktide, Matches: 2, Win Rate: 50.00%

### Deck: UB Murktide
  - Opponent: Amulet Titan, Matches: 1, Win Rate: 100.00%
  - Opponent: Goryo Atraxa, Matches: 1, Win Rate: 0.00%
  - Opponent: RG Breach/Eldrazi, Matches: 1, Win Rate: 0.00%
  - Opponent: UB Murktide, Matches: 2, Win Rate: 0.00%
