# 14. . Write a Python program to check whether a given string is a palindrome or not.

string = input("Enter the string: ")
palindrome = string[::-1]
if string != palindrome:
    print("not ", end = "")
print("palindrome")
