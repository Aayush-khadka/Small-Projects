print("\t\t\t\t ####*** Multiplication Guesser ***####")
print()

while True:
    num=int(input("Enter the Number you want to Play with:"))
    points=0
    again=""
    for a in range(1,11):
        user_guess=int(input(str(num)+" x "+ str(a)+" ="))
        if user_guess==num*a: 
            print("Right Answer")
            points +=1
        else:
            print("Wrong Answer, The Correct answer is ",num*a)
    print("=======================================")        
    print("you got ",points," out of 10 Right")
    print("=======================================")  
    a=input("Want to play again? (Y / N):")
    if a== "N":
        break
    print("--------------------------------------------------------")
