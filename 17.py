# 17. Write a Python function called factorial that calculates the factorial of a given number recursively.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    

num = int(input("Enter the number: "))
print(f"The factorial of {num} = {factorial(num)}")