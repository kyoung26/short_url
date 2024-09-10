import json
import random
import string

def generate_short_id():
    """Generating a random string consisting of 3 digits followed by 3 lowercase letters."""
    numbers = ''.join(random.choices(string.digits, k=3))
    letters = ''.join(random.choices(string.ascii_lowercase, k=3))
    return numbers + letters

def shorten_url(full_url):
    """Shortening the URL without validation."""
    short_id = generate_short_id()
    url_map[short_id] = full_url
    return f"https://myApp.com/{short_id}"

def get_full_url(short_id):
    """Retrieving the full URL from a shortened ID."""
    return url_map.get(short_id, "Shortened URL does not exist.")

def save_data():
    """Saving the dictionary to a JSON file."""
    with open('urls.json', 'w') as file:
        json.dump(url_map, file)

def load_data():
    """Loading the dictionary from a JSON file."""
    try:
        with open('urls.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Loading existing data
url_map = load_data()

# Simplified interface
while True:
    action = input("Choose an action: shorten (s) / retrieve (r) / quit (q): ").lower()
    if action == 'q':
        save_data()  # Saving before quitting
        break
    elif action == 's':
        url = input("Enter a URL to shorten: ")
        print("Shortened URL:", shorten_url(url))
    elif action == 'r':
        short_id = input("Enter the short ID to retrieve URL: ").split('/')[-1]  # Just in case the full short URL is pasted
        print("Original URL:", get_full_url(short_id))
    else:
        print("Invalid action.")