def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Get base and height from the studeny
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculating the area
area = calculate_triangle_area(base, height)


print(f"The area of the triangle with base {base} and height {height} is {area}")
