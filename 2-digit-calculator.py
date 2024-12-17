start = print(
    """
=====2 DIGIT CALCULATOR=====

"""
)


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("You can't divide by 0")
        return None
    return x / y


def calculator():
    while True:
        choiceType = input(r"What type of math do you want to do? (+\-\*\divide\exit) ")

        if choiceType == "+":
            x = input("Enter first number ")
            y = input("Enter number to add ")

            x = float(x)
            y = float(y)

            results = add(x, y)
            print(f"The sum of {x} and {y} is {results}")

        elif choiceType == "-":
            x = input("Enter the bigger number ")
            y = input("Enter the number you want to subtract ")

            x = float(x)
            y = float(y)

            results = minus(x, y)
            print(f"{x} minus {y} equals {results}")

        elif choiceType == "*":
            x = input("Enter the first number ")
            y = input("Enter the second number ")

            x = float(x)
            y = float(y)

            results = multiply(x, y)
            print(f"{x} times {y} equals {results}")

        elif choiceType == "divide":
            x = input("Enter the bigger number ")
            y = input("Enter the number to divide by ")

            x = float(x)
            y = float(y)

            results = divide(x, y)
            print(f"{x} divided by {y} equals {results}")

        elif choiceType == "exit":
            break
        else:
            print("Please enter a valid option")


calculator()
