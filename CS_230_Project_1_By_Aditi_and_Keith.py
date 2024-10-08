# Source Code for URL Shortner
# CS 230
# BY Aditi Jha and Keith Young

# Importing necessary libraries:
import json
import random
import string

import logging
import validators
import pyperclip
import tkinter as tk
from tkinter import simpledialog, messagebox

# Logging file, by Keith
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


'''Function generating short ID, Aditi 9/9/2024'''
def generate_short_id():
    """Generating a random string consisting of 3 digits followed by 3 lowercase letters."""
    numbers = ''.join(random.choices(string.digits, k=3))
    letters = ''.join(random.choices(string.ascii_lowercase, k=3))
    return numbers + letters

'''Function shortening the full URL to shortened URL, Aditi 9/9/2024'''
def shorten_url(full_url):
    """Shortening the URL without validation."""
    if not validators.url(full_url):
        return "Invalid URL"
    short_id = generate_short_id()
    while short_id in url_map:
        short_id = generate_short_id()
    url_map[short_id] = full_url
    return f"https://myApp.com/{short_id}"

'''Function retrieving full URL, Aditi 9/9/2024'''
def get_full_url(short_id):
    return url_map.get(short_id, "Shortened URL does not exist.")

'''Saving data to json file, Aditi 9/9/2024'''
def save_data():
    """Saving the dictionary to a JSON file."""
    with open('urls.json', 'w') as file:
        json.dump(url_map, file)
    logger.info("Saved file")
    
'''Exception handling, Aditi 9/9/2024'''
def load_data():
    """Loading the dictionary from a JSON file."""
    try:
        with open('urls.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

'''Function to count and list all URLs, Aditi 9/16/2024'''
def count_and_list_urls():
    url_count = len(url_map)
    if url_count == 0:
        messagebox.showinfo("URL Count", "No URLs stored.")
    else:
        urls_list = "\n".join([f"Shortened: https://myApp.com/{key} -> Original: {url_map[key]}" for key in url_map])
        messagebox.showinfo("URL Count", f"Total URLs: {url_count}\n\n{urls_list}")

url_map = load_data()

# Rate Limiting Implementation, Aditi Jha, 09/14/2024
request_count = 0
request_limit = 10   # Maximum number of requests per session

# Security feature: limit incorrect actions, Aditi Jha, 09/14/2024
incorrect_actions = 0
incorrect_action_limit = 3  # Maximum number of incorrect actions

# GUI Implementation, Aditi 9/16/2024
def gui_shorten_url():
    global request_count, incorrect_actions
    url = simpledialog.askstring("Input", "Enter a URL to shorten:")
    if url and validators.url(url):
        shortened_url = shorten_url(url)
        pyperclip.copy(shortened_url) # Copying the shortened URL to Clipboard, Aditi 9/16/2024
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
            pyperclip.copy(result)  # Copying the full URL to the clipboard, Aditi 9/16/2024
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
tk.Button(root, text="Count and List URLs", command=count_and_list_urls).pack(fill=tk.X)
tk.Button(root, text="Quit", command=quit_app).pack(fill=tk.X)

root.mainloop()



        
