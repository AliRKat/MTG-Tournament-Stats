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

```bash
python insert_tournament.py
python update_readme.py
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

PS: Huge thanks to https://readme.so/ editing README is always a pain in the ass

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
