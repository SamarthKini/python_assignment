# 9. Write a program that accepts a list of numbers from the user, then displays the list in ascending order, descending order, and calculates the sum and average of the numbers.
list = []
num = " "

while(len(num) != 0):
    num = input("Enter the number: ")
    try:
        number = int(num)
        list.append(number)
    except ValueError:
        break

list.sort()
print(f"Ascending order - {list}")
list.sort(reverse = True)
print(f"Descending order - {list}")
print(f"Sum - {sum(list)}")
print(f"Average - {sum(list)/len(list)}")