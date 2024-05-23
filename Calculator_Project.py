# Initialize the numbers
first_number = int(input("Give the first number: "))
second_number = int(input("Give the second number: "))

while True:
    # Print the main menu
    print("\n(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Change numbers")
    print("(6) Quit")
    print(f"Current numbers: {first_number} {second_number}")

    # Get the user's choice
    choice = int(input("Please select something (1-6): "))

    if choice == 1:
        result = first_number + second_number
        print(f"The result is: {result}")
    elif choice == 2:
        result = first_number - second_number
        print(f"The result is: {result}")
    elif choice == 3:
        result = first_number * second_number
        print(f"The result is: {result}")
    elif choice == 4:
        if second_number != 0:
            result = first_number / second_number
            print(f"The result is: {result}")
        else:
            print("Cannot divide by zero!")
    elif choice == 5:
        # Change the numbers
        first_number = int(input("Give the first number: "))
        second_number = int(input("Give the second number: "))
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice, please select a number between 1 and 6.")
