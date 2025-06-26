# calculator.py
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed"
    return n1 / n2

def calculator():
    print("Please select operation -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n")

    try:
        sel = int(input("Select operation (1-4): "))
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if sel == 1:
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif sel == 2:
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif sel == 3:
            print(f"{n1} * {n2} = {multiply(n1, n2)}")
        elif sel == 4:
            result = divide(n1, n2)
            print(f"{n1} / {n2} = {result}")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input: Please enter valid numbers")

if __name__ == "__main__":
    calculator()
