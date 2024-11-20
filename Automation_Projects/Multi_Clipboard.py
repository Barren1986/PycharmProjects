# This project will store multiple clipboard text and can be accessed by using a keyword.

# How to use:
# 1. Run the script with the following command:
#    python Multi_Clipboard.py save <keyword> - This will save the current clipboard text to the keyword.
#    python Multi_Clipboard.py get <keyword> - This will copy the clipboard text for the keyword to the clipboard.
#    python Multi_Clipboard.py list - This will list all the keywords.
# 2. The clipboard data will be stored in clipboard.json file.

import sys
import clipboard
import json

# Define the storage file
STORAGE_FILE = "clipboard.json"


def save_data(data):
    with open(STORAGE_FILE, 'w') as file:
        json.dump(data, file)


def load_data():
    try:
        with open(STORAGE_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_clipboard(keyword):
    data = load_data()
    data[keyword] = clipboard.paste()
    save_data(data)
    print(f"Data saved under keyword '{keyword}'.")


def get_clipboard(keyword):
    data = load_data()
    if keyword in data:
        clipboard.copy(data[keyword])
        print(f"Clipboard content for '{keyword}' copied to clipboard.")
    else:
        print(f"No data found for keyword '{keyword}'.")


def list_keywords():
    data = load_data()
    print("Stored keywords:")
    for keyword in data:
        print(f"- {keyword}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  save <keyword> - save current clipboard to keyword")
        print("  get <keyword>  - get clipboard text for keyword")
        print("  list           - list all keywords")
        return

    command = sys.argv[1]

    if command == "save" and len(sys.argv) == 3:
        save_clipboard(sys.argv[2])
    elif command == "get" and len(sys.argv) == 3:
        get_clipboard(sys.argv[2])
    elif command == "list":
        list_keywords()
    else:
        print("Invalid command or arguments.")


if __name__ == "__main__":
    main()