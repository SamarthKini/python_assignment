# 13. Write a Python function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.
vowels = ["a", 'e', 'i', 'o', 'u']
string = input("Enter the string: ")
count = 0
for i in string:
    if i in vowels:
        count += 1 
print(f"Vowel count = {count}")