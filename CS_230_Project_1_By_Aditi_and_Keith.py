import json
import random
import string
import logging
import validators

# Logging file

logging.basicConfig(
    filename="app.log",
    encoding= "utf-8",
    filemode= "a",
    format="{asctime} - {levelname} - {message}",
    style= "{",
    datefmt = "%Y -%m-%d %H:%M",
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
        if url.startswith("https://"):
            print("Shortened URL:", shorten_url(url))
        else:
            print("Can't do it!!!")
        logging.info("Got a short url!!!") # Sends "Got a short url!!!" to log file
    elif action == 'r':
        short_id = input("Enter the short ID to retrieve URL: ").split('/')[-1]  # Just in case the full short URL is pasted
        print("Original URL:", get_full_url(short_id))
        logging.info("Got back full url!!!") # Sends "Got back full url!!!" to log file
    else:
        print("Invalid action.")
        
        


        
