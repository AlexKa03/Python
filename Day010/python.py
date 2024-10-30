import art

def add(n1, n2):
    """This function is for adding 2 numbers."""
    return n1 + n2

def subtract(n1, n2):
    """This function is for subtracting 2 numbers."""
    return n1 - n2

def multiply(n1, n2):
    """This function is for multiplying 2 numbers."""
    return  n1 * n2

def divide(n1, n2):
    """This function is for dividing 2 numbers."""
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)

continue_with_new_number = "y"
first_number = float(input("What is your first number: "))

while continue_with_new_number != "exit":
    if continue_with_new_number == "n":
        first_number = float(input("What is your first number: "))

    for symbol in functions:
        print(symbol)
    operation = input("What mathematical operation do you want to perform: ")
    second_number = float(input("What is your second number: "))

    result = functions[operation](first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {result}")
    continue_with_new_number = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. If you want to exit type 'exit': ").lower()
    if continue_with_new_number == "y":
        first_number = result
    elif continue_with_new_number == "exit":
        print("You have exited the calculator app.")
    else:
        print("\n" * 20)
        print(art.logo)