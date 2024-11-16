#4. Write a Python program that simulates a simple login system. It should prompt the user for a password and allow three attempts to enter the correct password before displaying a "locked out" message.
needed_password = "password"
user_id = input("Enter the user id: ")
for i in range(3):
    password = input("Enter the password: ")
    if password == needed_password:
        exit()
    
print("locked out")