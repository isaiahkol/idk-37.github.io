"""
Isaiah Kol
ikol@uvm.edu
CEE1100C
Extra Credit - 2D Composite Centroid Wizard
"""


import math

def rectangle():    #Function which handles user input for rectangles and returns area and centroid coordinates.
    while True:    
        # Get rectangle information
        try:
            x1 = float(input("Enter x-coordinate of bottom-left corner: "))
            y1 = float(input("Enter y-coordinate of bottom-left corner: "))
            x2 = float(input("Enter x-coordinate of top-right corner: "))
            y2 = float(input("Enter y-coordinate of top-right corner: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    # Calculate area and centroid
    b = x2 - x1
    h = y2 - y1
    area = b * h
    xtilde = (x1 + x2) / 2
    ytilde = (y1 + y2) / 2
    # Return tuple of area and centroid coordinates for this shape
    return (area, xtilde, ytilde)

def triangle():     #Function which handles user input for triangles and returns area and centroid coordinates.
    while True:
        # Get triangle information
        try:
            x = float(input("Enter x-coordinate of right angle: "))
            y = float(input("Enter y-coordinate of right angle: "))
            b = float(input("Enter base length. Use (+) for right, (-) for left: "))
            h = float(input("Enter height. Use (+) for up, (-) for down: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    # Calculate area and centroid
    area = 0.5 * abs(b) * abs(h) # Using absolute values, as sign convention above is only for centroid location
    xtilde = x + (b / 3)
    ytilde = y + (h / 3)
    # Return tuple of area and centroid coordinates for this shape
    return (area, xtilde, ytilde)

def circle():   #Function which handles user input for circles/semicircles and returns area and centroid coordinates.
    while True:
        # Get circle information
        try:
            x = float(input("Enter x-coordinate of center: "))
            y = float(input("Enter y-coordinate of center: "))
            r = abs(float(input("Enter radius: ")))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    # Check if semicircle, then if indeed semicircle, calculate area and centroid based on orientation
    semi_query = input("Is this circle actually a semicircle? (YES or NO): ").upper()
    while semi_query not in ["YES", "NO"]:
        print("Invalid input. Please enter YES or NO.")
        semi_query = input("Is this circle actually a semicircle? (YES or NO): ").upper()
    if semi_query == "YES":
        semi_direction = input("Which way does the arc face? (UP, DOWN, LEFT, RIGHT): ").upper()
        if semi_direction == "UP":
            area = 0.5 * math.pi * r ** 2
            xtilde = x
            ytilde = y + (4 * r) / (3 * math.pi)
        elif semi_direction == "DOWN":
            area = 0.5 * math.pi * r ** 2
            xtilde = x
            ytilde = y - (4 * r) / (3 * math.pi)
        elif semi_direction == "LEFT":
            area = 0.5 * math.pi * r ** 2
            xtilde = x - (4 * r) / (3 * math.pi)
            ytilde = y
        elif semi_direction == "RIGHT":
            area = 0.5 * math.pi * r ** 2
            xtilde = x + (4 * r) / (3 * math.pi)
            ytilde = y
    # Otherwise calculate area and centroid for full circle
    else:
        area = math.pi * r ** 2
        xtilde = x
        ytilde = y
    # Return tuple of area and centroid coordinates for this shape
    return (area, xtilde, ytilde)

def get_shapes():   #Function which compiles a list of shapes which make up the composite shape. Calls shape functions above, and returns a list of tuples.
    # Establish empty list and counting variable
    shapes = []
    count = 1
    # Prompt for shapes, calling previous shape functions accordingly
    print("Please list the simple shapes that make up your complex composite shape.")
    print("Enter R for rectangle, T for triangle, C for circle (including semicircle), or 0 to exit.")
    while True:
        shape = input(f"What is shape #{count}: ").upper()
        while shape not in ["R", "T", "C", "0"]:
            print("Invalid shape type. Please enter R, T, or C, or 0 to exit.")
            shape = input(f"What is shape #{count}: ").upper()
            if shape == "0":
                break
        if shape == "0":
            break
        if shape == "R":
            (area, xtilde, ytilde) = rectangle()
        elif shape == "T":
            (area, xtilde, ytilde) = triangle()
        elif shape == "C":
            (area, xtilde, ytilde) = circle()
        # Check if indiviudal shape is a hole in the composite shape
        hole_query = input("If this shape is a hole in the composite shape, enter -; otherwise please enter +: ")
        if hole_query == "-":
            area = -area 
        shapes.append((area, xtilde, ytilde))
        count += 1 
    return shapes

def locate_centroid(shapes):  #Function which calculates and prints the final centroid (and additional component data) of the composite shape based on the list of shapes provided.
    # Establish summation variables for numerators and denominator of centroid formulas
    sum_area = 0
    sum_numerator_x = 0
    sum_numerator_y = 0
    # Iterate through shapes to calculate summations
    for area, xtilde, ytilde in shapes:
        sum_area += area
        sum_numerator_x += area * xtilde
        sum_numerator_y += area * ytilde
    # Calculate centroid coordinates
    xbar = sum_numerator_x / sum_area
    ybar = sum_numerator_y / sum_area
    # Print results
    print(f"\nThe centroid of your composite shape is located at ({xbar:.2f}, {ybar:.2f}){units}!")
    print("\nAdditional Stats:")
    print(f"The total area of your composite shape is {sum_area:.2f}{units}^2")
    for i, (area, xtilde, ytilde) in enumerate(shapes):
        print(f"Shape #{i+1}: Area = {area:.2f}{units}^2, Centroid = ({xtilde:.2f}, {ytilde:.2f}){units}")
    

if __name__ == "__main__":
    print("Welcome to the 2D Composite Centroid Wizard!")
    units = input("Please enter the units you will be using: ")
    shapes = get_shapes()
    if not shapes:
        print("No shapes were entered, exiting wizard.")
    else:
        locate_centroid(shapes)
