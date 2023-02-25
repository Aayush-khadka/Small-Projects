print("                 ### Guessing GAME ###")

exit=""
while exit != "yes":

    user_input=input("Which animal's Sound do you want:")
   

    if user_input == "cow" or user_input == "Cow":
        print("MOO MO")
    elif user_input == "Cat" or user_input == "cat":
        print("meow meow") 
    elif user_input == "Dog" or user_input == "dog":
        print("BHOW BHOW")
    else:
        print(" We dont have that Animal :(")
    
    print("")
    
    exit=input("Do you want to exxit:")
