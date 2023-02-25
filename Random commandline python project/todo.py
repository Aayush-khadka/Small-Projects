import os,time
todo_list=[]


def print_list():
    print("========TO DO list========")
    for a in range(len(todo_list)):

        print( (a+1),". ",todo_list[a])
    print("==========================")
    input("press ENTER to Move on:")

def entry():
    user_entry=input("What do you want to ADD?\n>> ")
    todo_list.append(user_entry.lower().strip().capitalize())
    print()

def change():
    item=input("Which Number do you like to Edit: ")
    edit=input('What do Would you like to change: ')
  
    for i in range(0,len(todo_list)):
        if todo_list[i]==todo_list[int(item)]:
            todo_list[i]=edit


def remove():
    user_entry=input("What do you want to remove?\n>> ")
    todo_list.remove(user_entry.strip().capitalize())   
    print()
    

while True:
    welcome="Welcome to Events Manager"
    print(f"{welcome:^70}")
  
    user_input=input("""\t\t\t
    1. View your List 
    2. Add item to List
    3. Remove item from  List
    4. Edit List
    5. Empty List
    6. Exit
    >>""")

    if user_input=="1":
            print_list()
            
    elif user_input=="2":
            entry()
            
    elif user_input=="3":
            remove()
                
    elif user_input=="4":
        change()

    elif user_input=="5":
        todo_list=[]
        
    elif user_input=="6":
        break
  
    else: 
        print("Please Select from the Options Above:")
    
    time.sleep(1)
    os.system("cls")





