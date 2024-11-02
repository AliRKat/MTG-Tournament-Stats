Welcome to the MTG Tournament Stats tool! This program helps me to track my performance in Magic: The Gathering tournaments by storing match results and generating statistics.


## Installation

```bash
git clone https://github.com/yourusername/MTGTournamentStats.git
cd MTGTournamentStats
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
    
## Usage/Examples

```bash
python insert_tournament.py
// this is always optional
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