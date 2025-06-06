import random
from .models import StatBlock, Character
from .storage import save_character, load_characters
from .dice import roll_dice

def create_character():
    name = input("Name: ")
    race = input("Race: ")
    char_class = input("Class: ")
    level = input("Level: ")
    if level == '':
        level = 1
    attr_vals = {}
    attr_vals["strength"] = (input("STR: "))
    attr_vals["dexterity"] = (input("DEX: "))
    attr_vals["constitution"] = (input("CON: "))
    attr_vals["intelligence"] = (input("INT: "))
    attr_vals["wisdom"] = (input("WIS: "))
    attr_vals["charisma"] = (input("CHA: "))

    for key, value in attr_vals.items():
        if value == '':
            attr_vals[key] = random.randint(1, 20)

    attributes = StatBlock(
        int(attr_vals["strength"]), int(attr_vals["dexterity"]), int(attr_vals["constitution"]),
        int(attr_vals["intelligence"]), int(attr_vals["wisdom"]), int(attr_vals["charisma"])
    )
    inventory = input("Inventory (comma separated): ").split(",")
    inventory = [item.strip() for item in inventory]
    character = Character(name, race, char_class, level, attributes, inventory)
    save_character(character)
    print(f"Character {name} saved!")

def edit_character():
    name = input("Enter the name of the character to edit: ")

    def update_fn(character):
        print(f"Editing {character.name} (Level {character.level})")
        new_level = input(f"Current level is {character.level}. New level (leave blank to keep): ")
        if new_level.strip().isdigit():
            character.level = int(new_level)

        new_inv = input("New inventory (comma separated, leave blank to keep current): ")
        if new_inv.strip():
            character.inventory = [item.strip() for item in new_inv.split(",")]

    from .storage import edit_character
    edit_character(name, update_fn)

def list_characters():
    characters = load_characters()
    for c in characters:
        print(f"'{c.name}' the Lvl {c.level} {c.race} {c.char_class}")

def roll_dice_cli():
    sides = int(input("Sides (e.g., 6, 20): "))
    count = int(input("How many dice? "))
    modifier = int(input("Modifier (e.g., +2): "))
    total, rolls = roll_dice(sides, count, modifier)
    print(f"Rolls: {rolls}, Total: {total}")

def main_menu():
    while True:
        try:
            print("\nD&D Character Manager")
            print("1. Create character")
            print("2. Edit characters")
            print("3. View characters")
            print("4. Roll dice")
            print("5. Exit")
            choice = input("Choose: ")
            match choice:
                case "1":
                    print("Creating a new character...")
                    create_character()
                case "2":
                    print("Editing an existing character...")
                    edit_character()
                case "3":
                    print("Listing all characters...")
                    list_characters()
                case "4":
                    print("Rolling dice...")
                    roll_dice_cli()
                case "5":
                    print("Exiting the program.")
                    break
                case _:
                    print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break