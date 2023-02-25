import time
import random
import os
def roll_dice(side):
    return random.randint(1,side)
def health():
     return round((roll_dice(6)*roll_dice(12)/2)+10)
def strength():
    return round((roll_dice(6)*roll_dice(8)/2)+12)
def main():
    print("\t\t\t CREATE YOUR CHARACTER")
    Charc_1_name=input("Enter The name of Your First Character: ")
    char_1_race=input('Enter The race of your Character (Human / Elf / Wizard):')
    char_1_health=health()
    print()
    Charc_2_name=input("Enter The name of Your Second Character: ")
    char_2_race=input('Enter The race of your Character (Human / Elf / Wizard):')
    char_2_health=health()
    time.sleep(1)
    os.system("cls")
    print("\t\t\tCHARACTER STATS")
    print("==================================")
    print(f'Name:{Charc_1_name}\nRace:{char_1_race}\nHealth:{char_1_health}\nStrength:{strength()}')
    print("==================================")
    print(f'Name:{Charc_2_name}\nRace:{char_2_race}\nHealth:{char_2_health}\nStrength:{strength()}')
    print("==================================")
    time.sleep(5)
    os.system("cls")
    print("\t\t\t  TIME FOR BATTLE ")
    print(f"\t\t\t Starting Health = {Charc_1_name}:{char_1_health} and {Charc_2_name}:{char_2_health}")
    print()
    while True:
        char_1_roll=roll_dice(6)
        char_2_roll=roll_dice(6)
        if char_1_roll>char_2_roll:
            print(f'It was  Tough BATTLE but {Charc_1_name} was able to snatch the Victory.\n{Charc_1_name} Pulled {char_1_roll} and {Charc_2_name} Pulled {char_2_roll}')
            char_2_health=char_2_health-char_1_roll
        elif char_2_roll>char_1_roll:
            print(f'It was  Tough Battle But {Charc_2_name} Was able to snatch the victory.\n{Charc_1_name} Pulled {char_1_roll} and {Charc_2_name} Pulled {char_2_roll}')
            char_1_health=char_1_health-char_2_roll
        print()
        print(f'Current Health:\n{Charc_1_name} health:{char_1_health}\n{Charc_2_name} health:{char_2_health}')
        
        print("===============================")
        if char_1_health<=0:
            
            print(f"It is a GLORIOUS VICTORY for {Charc_2_name} ")
            print("==========================================")
            break
        elif char_2_health<=0:
            
            print(f"It is a GLORIOUS VICTORY for {Charc_1_name} ")
            print("==========================================")
            break
        time.sleep(5)
        os.system("cls")
while True:
    main()
    a=input('Do you want to Batlle Again ( Y / N): ')
    if a=="N" or a=="NO":
        break
print()
input("\t\t\t\t\t\t\tPress ENTER to EXIT: ")

