
# Changes for task: Write code in the file to print "Hello World"
with open('hello_world.py', 'w') as file:
    file.write('print("Hello World")')

# Changes for task: Write code in the file to create a new text file named "hello_world.txt"
with open("hello_world.txt", "w") as file:
    file.write("Hello, World!")

# Changes for task: Write code in the file to write "Testing 123" to the "hello_world.txt" file
with open("hello_world.txt", "w") as file:
    file.write("Testing 123")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Python code to print "Hello World" and create a file "hello_world.txt" with the content "Hello World"

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Python code to print "Hello World" and create a file "hello_world.txt" with the content "Hello World"

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Python code to print "Hello World" and create a file "hello_world.txt" with the content "Hello World"

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Create hello_world.txt file with content
with open("hello_world.txt", "w") as file:
    file.write("Hello World\n")

# Print "Hello World"
print("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Python code to print "Hello World" and create a file "hello_world.txt" with the content "Hello World"

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Python code to print "Hello World" and create a file "hello_world.txt" with the content "Hello World"

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Write the Python code to print "Hello World" and create the "hello_world.txt" file with the correct content

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Execute the Python file to ensure it prints "Hello World" and creates the "hello_world.txt" file with the correct content
# Python code to print "Hello World" and create a file "hello_world.txt" with the content "Hello World"

print("Hello World")

with open("hello_world.txt", "w") as file:
    file.write("Hello World")

# Changes for task: Define a function that takes in the coefficients of a quadratic equation as input
def solve_quadratic(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real roots"

# Changes for task: Implement the quadratic formula within the function to calculate the roots of the equation
import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

# Example usage
a = 1
b = -3
c = 2
roots = quadratic_formula(a, b, c)
print(roots)

# Changes for task: Test the function with various input values to ensure it is calculating the correct roots
import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return complex(real_part, imaginary_part)

# Test the function with various input values
print(quadratic_roots(1, 0, -4))  # Expected output: (2.0, -2.0)
print(quadratic_roots(1, -6, 9))  # Expected output: 3.0
print(quadratic_roots(1, 2, 5))   # Expected output: (-1+2j)

# Changes for task: Handle edge cases such as when the discriminant is negative or when the coefficients are zero
import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("Coefficient 'a' cannot be zero")
    else:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            print("No real roots")
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print("Root 1:", x1)
            print("Root 2:", x2)

# Example usage
solve_quadratic(1, -3, 2)

# Changes for task: Add user input functionality to allow users to input their own coefficients for the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Quadratic formula
x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print("The solutions are: x1 =", x1, "and x2 =", x2)
