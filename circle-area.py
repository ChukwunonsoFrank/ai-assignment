# First, we define a function that implements the equation for the area of circle
def calculate_circle_area(radius):
    pi = 3.142
    area = pi * (radius ** 2)
    print(area)

# Then we call the function and pass in an argument representing the radius of the circle
calculate_circle_area(1)