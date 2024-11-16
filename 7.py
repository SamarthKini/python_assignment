# 7. Design a program that takes two integer inputs from the user and divides the first by the second. If the user enters zero as the second number, catch the exception and display an error message.

while(True):   
    num1 = int(input("Enter the number 1: "))     
    num2 = int(input("Enter the number 2: "))   
    try:
        num1/num2
    except ZeroDivisionError:
        print("Error: incorrect input")
        break