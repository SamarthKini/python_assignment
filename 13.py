# 13. Write a Python function called count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.

def count_vowels(string) -> int:
    vowels = ["a", 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

string = input("Enter the string: ")
print(f"Vowel count = {count_vowels(string)}")