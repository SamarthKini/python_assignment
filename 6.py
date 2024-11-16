#6. Write a program that repeatedly prompts the user to enter a number. If the user enters anything other than a number, display an error message and end the program.

while(True):        
    try:
        num = int(input("Enter the number: "))
    except ValueError:
        print("Error: incorrect input")
        break
   