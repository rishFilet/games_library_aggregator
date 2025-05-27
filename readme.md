# Steam Game Library Export Tool

A Python script that exports your Steam game library into a CSV file, including game names and their respective genres.

## Features

- Fetches your Steam game library using the Steam Web API
- Retrieves game genres by scraping the Steam store page
- Exports library data to a CSV file with platform, name, and genre columns
- Shows progress bar during data collection

## Prerequisites

- Python 3.x
- Required Python packages:
  - requests
  - beautifulsoup4
  - python-dotenv
  - tqdm

## Setup

1. Clone this repository
2. Create a `.env` file in the root directory with:
   ```
   STEAM_API_KEY=your_steam_api_key    # Get from https://steamcommunity.com/dev/apikey
   STEAM_ID=your_steam_id_64           # Your 64-bit Steam ID
   ```
3. Install required packages:
   ```
   pip install requests beautifulsoup4 python-dotenv tqdm
   ```

## Usage

Run the script:
`pipenv shell; python3 main.py`
