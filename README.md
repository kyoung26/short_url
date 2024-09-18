# CS 230 Project 1: URL Shortener

## Overview
This project provides a simple GUI application to shorten URLs using a Python script. It features URL shortening, validation, and retrieval functionalities, along with a basic GUI for user interaction. This application ensures that users can easily manage shortened URLs and retrieve the original URLs when needed. It also incorporates features like rate limiting and logging to handle usage limits and store activity logs, respectively.

## Features
- **URL Validation**: Ensures that only valid URLs are processed.
- **URL Shortening**: Converts a long URL into a shorter, manageable link.
- **URL Retrieval**: Retrieves the original URL using a short ID.
- **Data Persistence**: Saves and loads shortened URLs to and from a JSON file.
- **Rate Limiting**: Limits the number of requests a user can make in a session.
- **Incorrect Action Handling**: Limits the number of incorrect actions a user can perform before the application exits.
- **Duplication**: Handles duplicate URL.
- **Clipboard Copying**: Copies the shortened as well as the full URL (after retreival) to the clipboard for the user. 
- **Logging**: Logs various events such as URL shortening and application errors.
- **List and Count**: Lists and Count the shortened and retrieved URL.

## Installation
To set up the project, follow these steps:
1. Ensure that Python 3.7 or later is installed on your system.
2. Install the required Python packages: Validatos, pyperclip, tkinter
3. Clone this repository or download the project files to your local machine. And run the python script.

Follow the GUI prompts to shorten or retrieve URLs. The application supports basic interactions such as:
- **Shorten URL**: Input a valid URL to shorten it.
- **Retrieve URL**: Input a short ID to retrieve the original URL.
- **Quit**: Exit the application.

## Logging
All application activities are logged in `app.log`. This file includes timestamps and details of operations such as URL shortening and errors.

## Authors
- **Aditi Jha**
- **Keith Young**
