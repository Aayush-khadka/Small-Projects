from getpass import getpass
def login(username,password):
    if username=="Aayush" and password=="Aayush123":
        print("Welcome back,Aayush")
        return 0
    else:
        print("Wrong Username or password:")
        return 1
print("\t\t\t\t *** LOGIN ***")
while True:
    user_name=input("Username:")
    user_pass=getpass("password:")
    fed=login(user_name,user_pass)
    if fed==0:
        break