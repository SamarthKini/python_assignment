#5. Define a function is_even(number) that returns True if a number is even and False if it’s odd. Then write a program to take an integer input, call this function, and display whether the number is even or odd.


def is_even(num):
    if num % 2 == 0:
        return True
    return False

num = int(input("Enter the number: "))
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
        