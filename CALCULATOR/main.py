from art import logo
print(logo)


# Add
def add(n1, n2):
    return n1+n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n1

# Divide
def divide(n1, n2):
    return n1/n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide
}
to_continue = True
while to_continue:
    num1 = int(input("What's the first Number?: "))
    num2 = int(input("What's the second Number?: "))
    for symbol in operators:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    calculation_function = operators[operation_symbol]
    result = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    another_one = input("Do you wish to perform another operation? Press 'yes' or 'no'. ")
    if another_one == "no":
        print("Thanks for Using me.❤️ ")
        to_continue = False
    elif another_one == "yes":
        continue


