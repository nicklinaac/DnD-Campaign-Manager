class StatBlock:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def to_dict(self):
        return self.__dict__

class Character:
    def __init__(self, name, race, char_class, level, attributes, inventory=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        self.attributes = attributes  # StatBlock instance
        self.inventory = inventory if inventory else []

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "level": self.level,
            "attributes": self.attributes.to_dict(),
            "inventory": self.inventory
        }

    @staticmethod
    def from_dict(data):
        attributes = StatBlock(**data['attributes'])
        return Character(
            name=data['name'],
            race=data['race'],
            char_class=data['class'],
            level=data.get('level', 1),
            attributes=attributes,
            inventory=data.get('inventory', [])
        )