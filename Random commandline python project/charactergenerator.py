import random
import os
import time
while True:
    print("\t\t\t\tWELCOME TO CHARACTER CREATOR")
    character_name=input("Enter your Character's Name: ")
    character_race=input("What Race is your Character (Human / Elf / Dwarves):")
    health=round((random.randint(1,6)*random.randint(1,12))/2+10)
    strength=round((random.randint(1,6)*random.randint(1,12))/2+12)
    print("=========================")
    print(f"Name:{character_name}\nRace:{character_race}\nHealth:{health}\nStrenght:{strength}")
    print("=========================")
    print()
    a=input("Want to Create Another Character (Y / N):")
    if a== "N":
        break
    
    time.sleep(1)
    os.system("cls")

input("Press Enter to EXit:")
