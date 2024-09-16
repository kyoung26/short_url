import json
import random
import string
import logging
import validators
import pyperclip
import tkinter as tk
from tkinter import simpledialog, messagebox

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
request_limit = 10   # Maximum number of requests per session

# Security feature: limit incorrect actions, Aditi Jha, 09/14/2024
incorrect_actions = 0
incorrect_action_limit = 3  # Maximum number of incorrect actions


# GUI Implementation
def gui_shorten_url():
    global request_count, incorrect_actions
    url = simpledialog.askstring("Input", "Enter a URL to shorten:")
    if url and validators.url(url):
        shortened_url = shorten_url(url)
        pyperclip.copy(shortened_url)
        messagebox.showinfo("Result", f"Shortened URL: {shortened_url}\nURL copied to clipboard.")
        logger.info("Shortened a URL.")
        request_count += 1
    else:
        messagebox.showerror("Error", "Invalid URL format. Please ensure it starts with 'https://'.")
        handle_incorrect_action()

def gui_get_full_url():
    global request_count, incorrect_actions
    short_id = simpledialog.askstring("Input", "Enter the short ID to retrieve URL:")
    if short_id:
        result = get_full_url(short_id)
        if result == "Shortened URL does not exist.":
            messagebox.showerror("Error", result)
            handle_incorrect_action()
        else:
            pyperclip.copy(result)  # Copying the full URL to the clipboard
            messagebox.showinfo("Result", f"Original URL: {result}\nURL copied to clipboard.")
        request_count += 1
    else:
        handle_incorrect_action()

def handle_incorrect_action():
    global incorrect_actions
    incorrect_actions += 1
    if incorrect_actions >= incorrect_action_limit:
        messagebox.showwarning("Error", "Maximum incorrect attempts exceeded. Exiting the application.")
        save_data()
        root.destroy()

def quit_app():
    save_data()
    root.destroy()

# Main GUI Window
root = tk.Tk()
root.title("URL Shortener")

# Adding buttons
tk.Button(root, text="Shorten URL", command=gui_shorten_url).pack(fill=tk.X)
tk.Button(root, text="Retrieve URL", command=gui_get_full_url).pack(fill=tk.X)
tk.Button(root, text="Quit", command=quit_app).pack(fill=tk.X)

root.mainloop()



        
