# 16. . Write a Python function called is_prime that takes an integer as input and returns True if the number is prime, otherwise False.
def is_prime(num):
    num1 = num 
    count = 0

    while(num1 > 0):
        if num % num1 == 0:
            count += 1 
        num1 -= 1

    if count > 2:
        return "not "
    else: 
        return ""


num = int(input("Enter the number: "))
print(f"The entered number is {is_prime(num)}a prime number")

    