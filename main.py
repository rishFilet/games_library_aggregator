import csv
import os
import requests
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv(override=True)

# Replace with your actual Steam API key and SteamID64
STEAM_API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")


# Epic Games requires authentication and scraping, so we'll use a workaround below


def get_steam_games(api_key, steam_id):
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&include_appinfo=1&format=json"
    response = requests.get(url)
    data = response.json()
    games = data.get("response", {}).get("games", [])
    game_details = []
    for game in tqdm(games, desc="Getting Steam games"):
        appid = game["appid"]
        name = game["name"]
        genre = get_steam_game_genre(appid)
        game_details.append({"platform": "Steam", "name": name, "genre": genre})
    return game_details


def get_steam_game_genre(appid):
    try:
        url = f"https://store.steampowered.com/app/{appid}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        genre_tags = soup.select('.details_block a[href*="genre"]')
        genres = [tag.text for tag in genre_tags]
        return ", ".join(genres)
    except Exception:
        return "Unknown"


def export_to_csv(game_list, filename="game_library.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["platform", "name", "genre"])
        writer.writeheader()
        for game in game_list:
            writer.writerow(game)


if __name__ == "__main__":
    steam_games = get_steam_games(STEAM_API_KEY, STEAM_ID)
    all_games = steam_games
    export_to_csv(all_games)
    print("Export completed. Saved as game_library.csv")
