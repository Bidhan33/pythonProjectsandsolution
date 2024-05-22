
def calculator():
    print("Calculator")

    num1 = int(input("Give the first number: "))

    num2 = int(input("Give the second number: "))

    # Display operation options
    print("(1) +\n(2) -\n(3) *\n(4) /")

    # Input operation choice
    choice = input("Please select something (1-4): ")

    # Perform the selected operation
    if choice == '1':
        print("The result is:", num1 + num2)
    elif choice == '2':
        print("The result is:", num1 - num2)
    elif choice == '3':
        print("The result is:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print("The result is:", num1 / num2)
    else:
        print("Selection was not correct.")


calculator()
