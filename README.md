# MTG-Tournament-Stats

Welcome to the MTG Tournament Stats tool! This program helps me to track my performance in Magic: The Gathering tournaments by storing match results and generating statistics.

## Getting Started

- **Installation:**
   ```bash
   git clone https://github.com/yourusername/MTGTournamentStats.git
   cd MTGTournamentStats
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

## Usage
    ```bash
    python insert_match.py
    python update_readme.py

## Features
    Track matches and tournaments with detailed stats.
    Easy-to-use command-line interface.
    Automatically calculate win rates against different decks.

## Database Structure
    * This tool uses SQLite for data storage, maintaining the following tables:
    * Decks: Records all decks played.
    * Matches: Stores match results, including player and opponent details.

## Stats Overview
- Total matches played: 6
- Decks I played:
  - Mono Blue Tron: 6 matches
- Decks I played against (win rate):
  - Amulet Titan: 1 matches, Win Rate: 100.00%
  - Boros Energy: 1 matches, Win Rate: 0.00%
  - Domain Zoo: 1 matches, Win Rate: 0.00%
  - RG Breach/Eldrazi: 1 matches, Win Rate: 100.00%
  - UB Frogtide: 2 matches, Win Rate: 50.00%
