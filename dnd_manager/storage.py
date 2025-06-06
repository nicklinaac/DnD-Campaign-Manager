import json
import os

CHAR_DIR = "characters"

def save_character(character):
    os.makedirs(CHAR_DIR, exist_ok=True)
    file_path = os.path.join(CHAR_DIR, f"{character.name.lower()}.json")
    with open(file_path, "w") as f:
        json.dump(character.to_dict(), f, indent=4)

def load_characters():
    characters = []
    if not os.path.exists(CHAR_DIR):
        return characters
    for file in os.listdir(CHAR_DIR):
        with open(os.path.join(CHAR_DIR, file)) as f:
            from .models import Character
            data = json.load(f)
            characters.append(Character.from_dict(data))
    return characters

def edit_character(name, update_fn):
    """Load a character by name, allow updates via update_fn, and save."""
    file_path = os.path.join(CHAR_DIR, f"{name.lower()}.json")
    if not os.path.exists(file_path):
        print(f"Character '{name}' not found.")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    from .models import Character
    character = Character.from_dict(data)

    # Allow caller to update the character
    update_fn(character)

    with open(file_path, "w") as f:
        json.dump(character.to_dict(), f, indent=4)
    print(f"Character '{name}' updated.")