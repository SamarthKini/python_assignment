#3. Write a program that takes an integer input from the user. Check if the number is positive, negative, or zero and display the result.
num = int(input("Enter the number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")