import random

def roll_dice(sides, count=1, modifier=0):
    try:
        rolls = [random.randint(1, sides) for _ in range(count)]
        return sum(rolls) + modifier, rolls
    except ValueError as e:
        raise ValueError(f"Invalid input for dice roll: {e}") from e
