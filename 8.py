# 8. Implement a number-guessing game where the program randomly selects a number between 1 and 100. The user has seven attempts to guess the number. After each guess, the program should tell the user if the guess is too high, too low, or correct. Use functions to structure the program.
import random

answer = random.randint(1, 100)
for i in range(7):
        num = int(input("Guess the number: "))
        if num < answer:
            print("Too low")
        elif num > answer:
            print("Too high")
        else:
            print("Correct")
            break
