
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
