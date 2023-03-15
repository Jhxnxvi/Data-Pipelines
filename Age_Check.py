# range check
try:
    age = int(input("Please enter your age: "))
    if age >= 13 and age <= 19:
        print("You are a teenager!")
    else:
        print("You are not a teenager.")
except ValueError:
    print("Invalid input. Please enter an integer.")