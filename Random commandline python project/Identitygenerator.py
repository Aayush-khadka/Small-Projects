import random
first_name=['Aayush','Sabin','Abhaya','Birat','Chetan','Sagar']
second_name=['Khadka','Bhattrai','kumal','Neupane','Adhakari']
address=['Damak','Birtamod','Ithari','Dharan','Kathmandu','Pokhara']
language=['Hindi', 'English','German','Japanese',"Nepali",'Korean']

print("\t\t\t\t\t **** Fake Identity Generator ****")

n=int(input("\tHow mant Fake identity do you Want: "))
print("=========================")


for a in range(n):
        first=random.choice(first_name)
        last=random.choice(second_name)

        phone= f'98-{random.randint(10000000, 99999999)}'

        address_P=random.choice(address)
        language_p=random.sample(language,k=2)

        print(f"First Name:{first} {last}\nPhone no:{phone}\nAddress:{address_P}\nLanguages:{language_p}")
        print("=========================")

input('\t\t\tPress ENTER to exit')