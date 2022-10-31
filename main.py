contn = True
while contn:
    print ("Welcome to the Calculator")
    num1 = float (input("Please write the first number: "))
    num2 = float (input("Please write the second number: "))
    contn2 = True
    operation = input("Choose an operation: 1 is for +, 2 is for -, 3 is for *, 4 is for /: ")

    while contn2:
        contn2 = False
        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 * num2
        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero!"
        else:
            result = "Unknown option."
            contn2 = True

    print(result)

