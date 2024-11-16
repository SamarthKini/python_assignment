# 10. Create a Magic 8 Ball program that stores several responses (e.g., "Yes," "No," "Maybe") in a list. When run, the program should display a random response from the list.
import random
list = []
for i in range(8):
    response = input(f"Enter the response {i + 1}: ")
    list.append(response)

print(list[random.randint(0,7)])