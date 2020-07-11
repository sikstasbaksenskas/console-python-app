import random


class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class Character:
    characterNames = ['Luke', 'David', 'Carter', 'Jace', 'Cooper', 'Evie', 'Lyric', 'Gabriela', 'Madilyn', 'Talia']

    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = random.choice(self.characterNames)
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hitpoints = constitution * 10

    def getAllInformation(self):
        # Prints all the information about character
        print(f"{bcolors.OKBLUE}Name: " + str(self.name) 
        +  ", Strength: " + str(self.strength) 
        +  ", Dexterity: " + str(self.dexterity)
        +  ", Constitution: " + str(self.constitution)
        +  ", Intelligence: " + str(self.intelligence)
        +  ", Wisdom: " + str(self.wisdom)
        +  ", Charisma: " + str(self.charisma)
        +  ", Hitpoints: " + str(self.hitpoints))
        print("-----------------------------------------")

    def getName(self):
        # Returns the name of the character
        return self.name


def collectInformation():
    # Collect data about character if user chooses to create charater manually
    stats = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
    for x in stats:
        while True:
            try:
                val = int(input('Please enter ' + x + ' points for your character(1-6): '))
                if 1 <= val <= 6:
                    stats[x] = val
                    break
            except (ValueError, TypeError):
                pass
    return createCharacter(stats)

def generateInformation():
    # Generate all information for the character if user chooses to create character randomly
    stats = {
        'STR': random.randint(1,6), 
        'DEX': random.randint(1,6), 
        'CON': random.randint(1,6), 
        'INT': random.randint(1,6), 
        'WIS': random.randint(1,6), 
        'CHA': random.randint(1,6)
        }
    return createCharacter(stats)

def createCharacter(info):
    # Create character
    return Character(info['STR'], info['DEX'], info['CON'], info['INT'], info['WIS'], info['CHA'])

def main():
    charactersList = {}

    while True:
        # Main MENU
        print(f"{bcolors.OKBLUE}Main menu:{bcolors.ENDC}")
        print("Enter 1 to create character manually: ")
        print("Enter 2 to create character randomly: ")
        print("Enter 3 to print all created characters: ")
        print("Enter 4 to print character's information by the name(Enter 3 in main menu to see the names): ")
        print("Enter 5 to exit: ")
        print("-----------------------------------------")

        choice = input ("Please make a choice: ")

        if choice == "1":
            # Creating object of character also adding it to the dictionary 
            character = collectInformation()
            charactersList[character.getName()] = character
            print(f"{bcolors.OKGREEN}Character has been created!{bcolors.ENDC}")
        elif choice == "2":
            # Creating object of character also adding it to the dictionary 
            character = generateInformation()
            charactersList[character.getName()] = character
            print(f"{bcolors.OKGREEN}Character has been created!{bcolors.ENDC}")
        elif choice == "3":
            # Prints all the names of the characters from the dictionary
            print(f"{bcolors.OKBLUE}List of all characters:{bcolors.ENDC}")
            for obj in charactersList:
                print(obj)
        elif choice == "4":
            # If you enter the name of the character that exists in the dictionary 
            # it will output all the information about that character
            name = input("Please enter the name of the character: ")
            if name in charactersList:
                print(charactersList[name].getAllInformation())
            else:
                print(f"{bcolors.WARNING}There is no such name in the list of characters!{bcolors.ENDC}")
        elif choice == "5":
            # Exit
            break
        else:
            print(f"{bcolors.WARNING}I don't understand your choice. Please choose again!{bcolors.ENDC}")
    print("Bye!")

main()
