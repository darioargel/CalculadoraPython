def add(n1, n2):
    return n1 + n2

def calculator():
    print("Calculadora: Suma")
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        print(f"{n1} + {n2} = {add(n1, n2)}")
    except ValueError:
        print("Invalid input: Please enter valid numbers")

if __name__ == "__main__":
    calculator()
