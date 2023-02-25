import random
name=input("Enter your Name: ")
wc_list=["hola","bonjour","guten tag","salve","nǐn hǎo","olá","asalaam alaikum","konnichiwa","anyoung haseyo","Zdravstvuyte"]
r=random.randint(1,len(wc_list))

print(f"{wc_list[r]},{name}")