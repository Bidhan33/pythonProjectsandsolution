def authenticate():
    correct_name = "John"
    correct_password = "ABC123"

    # Ask for the user name
    name = input("Give name: ")

    if name != correct_name:
        print("The given name is wrong.")
    else:
        # Ask for the password
        password = input("Give password: ")

        if password == correct_password:
            print("Both inputs are correct!")
        else:
            print("The password is incorrect.")

# Run the authentication function
authenticate()
