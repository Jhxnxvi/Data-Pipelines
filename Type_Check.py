# Type Check
valid_input = False

while not valid_input:
    user_input = input("Please enter an integer: ")

# Checking if the input is an integer
    if user_input.isdigit():
        valid_input = True
    else:
        print("Invalid input. Please enter an integer.")

print("Input value:", int(user_input))
