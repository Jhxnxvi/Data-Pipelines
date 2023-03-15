valid_input = False

while not valid_input:
    password = input("Please enter a password (at least 6 characters long): ")
    if len(password) >= 6:
        valid_input = True
    else:
        print("Password too short. Please enter a password that is at least 6 characters long.")

print("Password:", password)
