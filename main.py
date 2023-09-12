import requests
import os
import time
from config import BITLY_URL, BITLY_HEADERS, BITLY_ACCESS_TOKEN

# Function to shorten a URL
def shorten_url(long_url, url, headers):
    data = {
        "long_url": long_url,
        "group_guid": None,
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        short_url = response.json()["link"]
        return short_url
    else:
        return None, response.json().get("description", "An unexpected error occurred.")

# Function to clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Display the main menu with a touch of humor
def main_menu():
    print("\033[1;36mBitly URL Shortener\033[0m")
    print("\033[1;33m-------------------\033[0m")
    print("Welcome to the Bitly URL Shortener!")
    print("Before you start, please read the README for instructions.")
    print("If you need help, type 'help' or 'readme' anytime to see this message again.")
    print("\033[1;37mReplit | Made by WiiZARDD\033[0m")

# Display the main menu options
def display_menu():
    print("\033[1;34mMenu:\033[0m")
    print("1. Shorten a URL")
    print("2. Expand a Short URL")
    print("3. View Shortened URLs")
    print("4. Exit")

# Display error messages with a humorous twist
def display_error_message(error_message):
    print("\033[1;31mERROR: {}\033[0m".format(error_message))

# Implement a countdown timer for added suspense
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print("\033[1;37mReturning to the menu in {:2d} seconds...  \033[0m".format(i), end="\r")
        time.sleep(1)

# Display a list of shortened URLs
def display_shortened_urls(shortened_urls):
    if not shortened_urls:
        print("No URLs have been shortened yet.")
    else:
        print("Shortened URLs:")
        for idx, url in enumerate(shortened_urls, start=1):
            print("{}. {}".format(idx, url))

# Function to expand a shortened URL
def expand_url(short_url):
    response = requests.get(short_url, allow_redirects=False)
    if response.status_code == 301 or response.status_code == 302:
        expanded_url = response.headers["Location"]
        return expanded_url
    else:
        return None, "Failed to expand URL: The provided short URL is invalid."

if __name__ == "__main__":
    shortened_urls = []
    
    while True:
        clear_screen()
        main_menu()
        display_menu()
        choice = input("\033[1;35mEnter your choice: \033[0m")

        if choice == "1":
            if BITLY_ACCESS_TOKEN == "YOUR_BITLY_ACCESS_TOKEN":
                display_error_message("You must set your Bitly access token in the configuration.")
                print("Please fork the project and replace 'YOUR_BITLY_ACCESS_TOKEN' with your access token.")
                countdown_timer(5)
            else:
                clear_screen()
                main_menu()
                long_url = input("\033[1;37mEnter the URL you want to shorten: \033[0m")
                short_url, error_message = shorten_url(long_url, BITLY_URL, BITLY_HEADERS)
                if short_url:
                    shortened_urls.append(short_url)
                    print("\033[1;32mShortened URL: {}\033[0m".format(short_url))
                else:
                    clear_screen()
                    main_menu()
                    display_error_message("Failed to shorten URL: {}".format(error_message))
                    countdown_timer(5)
        elif choice == "2":
            clear_screen()
            main_menu()
            if not shortened_urls:
                display_error_message("No shortened URLs available for expansion.")
                countdown_timer(5)
                continue
            print("Select a shortened URL to expand:")
            display_shortened_urls(shortened_urls)
            selection = input("\033[1;35mEnter the number of the URL to expand: \033[0m")
            try:
                selected_idx = int(selection) - 1
                if 0 <= selected_idx < len(shortened_urls):
                    expanded_url, error_message = expand_url(shortened_urls[selected_idx])
                    if expanded_url:
                        print("\033[1;32mExpanded URL: {}\033[0m".format(expanded_url))
                    else:
                        display_error_message(error_message)
                else:
                    display_error_message("Invalid selection. Please choose a valid number.")
            except ValueError:
                display_error_message("Invalid input. Please enter a number.")
            countdown_timer(5)
        elif choice == "3":
            clear_screen()
            main_menu()
            display_shortened_urls(shortened_urls)
            countdown_timer(5)
        elif choice == "4":
            clear_screen()
            print("\033[1;36mGoodbye!\033[0m")
            break
        elif choice.lower() in ("help", "readme"):
            if BITLY_ACCESS_TOKEN == "YOUR_BITLY_ACCESS_TOKEN":
                display_error_message("You must set your Bitly access token in the configuration.")
                print("Please fork the project and replace 'YOUR_BITLY_ACCESS_TOKEN' with your access token.")
                countdown_timer(5)
            else:
                clear_screen()
                main_menu()
                print("Before you continue, please read the README for instructions.")
                countdown_timer(5)
        else:
            clear_screen()
            main_menu()
            display_error_message("Invalid choice. Please try again.")
            countdown_timer(5)

    print("\033[1;33m-------------------\033[0m")
    print("\033[1;37mMADE BY WiiZARDD\033[0m")
    print("\033[1;37mReplit | Made by WiiZARDD\033[0m")
