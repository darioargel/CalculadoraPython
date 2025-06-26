def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed"
    return n1 / n2

def calculator():
    print("Calculadora: División")
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        result = divide(n1, n2)
        print(f"{n1} / {n2} = {result}")
    except ValueError:
        print("Invalid input: Please enter valid numbers")

if __name__ == "__main__":
    calculator()
