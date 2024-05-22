number_1 = int(input("Give a number : "))
number_2 =int( input("Give another number: "))

if number_1 % 2 == 0 and number_2 % 2 == 0:
    print("Both numbers are even.")
elif number_1 % 2 == 0 or number_2 % 2 == 0:
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")