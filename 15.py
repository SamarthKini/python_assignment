# 15. Write a Python function called calculate_circle_area that takes the radius of a circle as input and returns its area.


def calculate_circle_area(radius):
    return 3.142 * radius

radius = float(input("Enter the radius of the circle: "))
print(f"Area of circle = {calculate_circle_area(radius)}")
