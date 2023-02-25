print("                                 ###** ROCK-PAPER-SCISSORS **####")
print("""
                                                ROCK - R
                                                PAPER- P
                                                SCISSORS - S
""")
print("----------------------------------")
p1_nam=input("Enter Player one's name: ")
p2_nam=input("Enter Player two's name: ")
print("----------------------------------")
p1_count=0
p2_count=0
while True:
    if p2_count == 3:
        print("==================================")
        print(p2_nam+" WINS THE BEST FO THREE")
        print("==================================")
        exit()
    elif p1_count==3:
        print("==================================")
        print(p1_nam+" WINS THE BEST OF THREE")
        print("==================================")
        exit()
    else:
    
        p1=input(p1_nam +" Enter your move:")
        p2=input(p2_nam +" Enter your move: ")
        print("==================================")
        print()
        if p1=="R":
            print("It was a very Intense match between "+p1_nam+" and "+p2_nam+ " but ")
            if p2=="S":
                print(p1_nam+"'s Rock DESTROYS "+p2_nam+"'s Scrissors and "+ p1_nam+" WINS!!")
                p1_count +=1
            if p2=="P":
                print(p1_nam+ "'s Rock is WRAPPED by "+p2_nam+ "'s papper and "+p2_nam+" WINS!!!")
                p2_count +=1
            if p2=="R":
                print(p1_nam+"'s Rock is stopped by "+p2_nam+"'s Rock turning in to sand and it's a DRAW!!")
        elif p1=="P":
            print("It was a very Intense match between "+p1_nam+" and "+p2_nam+ " but ")
            if p2=="S":
                print(p1_nam+"'s paper is cut down in to many pieces by"+p2_nam+"'s scissors. "+p2_nam+" WINS!!")
                p2_count +=1
            if p2=="P":
                print("IT'S A DRAWW !!!!!!!!!!!")
            if p2=="R":
                print(p1_nam+"'s paper wraps around "+p2_nam+"'s Rock and "+p1_nam+" WINS!!!")
                p1_count +=1
        elif p1=="S":
            print("It was a very Intense match between "+p1_nam+" and "+p2_nam+ " but ")
            if p2=="S":
                print("IT'S A DRAWW !!!!!!!")
            if p2=="P":
                print(p2_nam+"'s Paper is made in several pieces by "+p1_nam+"'s SCISSORS. an it's a WIN For"+p1_nam)
                p1_count +=1
            if p2=="R":
                print(p1_nam+"'s Scissors in smashed in to pieces by "+p2_nam+"'s Rock. It's a WIN for "+p2_nam)
                p2_count +=1
        else:
            print("Wrong Entry  :( ")
        print()
        print()




