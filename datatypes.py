import random

name = input("Enter you characters's name: ")
power = input("Enter your character's class: ")
age = int(input("Enter your character's age: "))
height = input("Enter your character's height in cm: ")
inventory = ("Health Potion","Dagger","Rope","Ladder","Katana")
random_number = random.randint(1,4)
random_str = random.randint(70,100)
random_int = random.randint(70,100)
random_agi = random.randint(70,100)
if power == "Mage":
    is_magic_user = True
else:
    is_magic_user = False

print(f'''Generating stats...\t
      
      
Character Profile:
------------------
      
Name        : {name}
Class       : {power}
Age         : {age}
Height      : {height}
Magic User  : {is_magic_user}
Weapon      : {inventory[random_number]}
Strength    : {random_str}
Intelligence: {random_int}
Agility     : {random_agi}
''')




