print("                     ### GUESS the Lyrics ### ")
counter=1
while True:
    
    user_input=input("Never Gonna ______ you up:   ")
    if user_input == "give" or user_input == "Give":
        print()
        print("     AYY.. right Choice. It took you",counter,"Attempt")
        print()
        again=input("Exit?:")
        if again == "no":
            break
    else:
        counter += 1
        print()
        print("       Wrong Choice, mate")
        print()
        again=input("Want to try again")
        print("---------------------------------------")
        if again == "no":
            break