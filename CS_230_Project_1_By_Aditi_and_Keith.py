import json
import random
import string
import logging
import validators
import pyperclip  


# Logging file

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_short_id():
    """Generating a random string consisting of 3 digits followed by 3 lowercase letters."""
    numbers = ''.join(random.choices(string.digits, k=3))
    letters = ''.join(random.choices(string.ascii_lowercase, k=3))
    return numbers + letters
"""Added code that checks if url already exists"""
"""Keith Young 9/10/24"""

def shorten_url(full_url):
    """Shortening the URL without validation."""
    """Long id is mapped to short id. Ex: short_id [long_id]"""
    """Following code makes sure that the user has entered a valid URL - Aditi - 9/11/24"""
    if not validators.url(full_url):
        return "Invalid URL"
    short_id = generate_short_id()
    while short_id in url_map:
        short_id = generate_short_id()
    url_map[short_id] = full_url
    return f"https://myApp.com/{short_id}"


def get_full_url(short_id):
    """Retrieving the full URL from a shortened ID."""
    return url_map.get(short_id, "Shortened URL does not exist.")

def save_data():
    """Saving the dictionary to a JSON file."""
    """Message of saved filed gets sent to log file"""
    with open('urls.json', 'w') as file:
        json.dump(url_map, file)
    logger.info("Saved file")
    
def load_data():
    """Loading the dictionary from a JSON file."""
    try:
        with open('urls.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

url_map = load_data()

# Rate Limiting Implementation, Aditi Jha, 09/14/2024
request_count = 0
request_limit = 10  # Maximum number of requests per session

# Security feature: limit incorrect actions, Aditi Jha, 09/14/2024
incorrect_actions = 0
incorrect_action_limit = 3  # Maximum number of incorrect actions

# Simplified interface
while True:
    if incorrect_actions >= incorrect_action_limit:
        print("Maximum incorrect attempts exceeded. Please restart the application.")
        break

    action = input("Choose an action: shorten (s) / retrieve (r) / quit (q): ").lower()
    if action == 'q':
        save_data()  # Saving before quitting
        break
    elif action == 's':
        url = input("Enter a URL to shorten: ")
        if validators.url(url):
            shortened_url = shorten_url(url)
            print("Shortened URL:", shortened_url)
            pyperclip.copy(shortened_url)  # Copying the shortened URL to the clipboard, Aditi Jha, 09/14/2024
            print("URL copied to clipboard.")
            logger.info("Shortened a URL.")
            request_count += 1
        else:
            print("Invalid URL format. Please ensure it starts with 'https://'.")
            incorrect_actions += 1
    elif action == 'r':
        short_id = input("Enter the short ID to retrieve URL: ").split('/')[-1]
        result = get_full_url(short_id)
        if result == "Shortened URL does not exist.":
            print(result)
            incorrect_actions += 1
        else:
            print("Original URL:", result)
        request_count += 1
    else:
        print("Invalid action.")
        incorrect_actions += 1  # Incrementing on any invalid menu action



        
