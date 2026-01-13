user_name = ["aman", "kapil", "sachin"]
passw = [123, 456,789]
user = input("Enter user name :")
password = eval(input("Enter password :"))

if user in user_name and password in passw:
    print("User exist")
else :
    print("user not exist")    


