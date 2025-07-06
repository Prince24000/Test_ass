
def addition(a: float, b: float) -> float:
    return a + b

def subtraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    return a / b

def get_number(prompt: str) -> float:
    """Prompt the user for a number, or exit if they type 'exit'."""
    while True:
        entry = input(prompt).strip().lower()
        if entry in ('exit', 'e'):
            print("Goodbye!")
            exit(0)
        try:
            return float(entry)
        except ValueError:
            print("That’s not a valid number. Try again or type 'exit' to quit.")

def get_operator() -> str:
    """Prompt the user for an operator, or exit if they type 'exit'."""
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Enter operator (+, -, *, /) or 'exit' to quit: ").strip().lower()
        if op in ('exit', 'e'):
            print("Goodbye!")
            exit(0)
        if op in valid_ops:
            return op
        print(f"Invalid operator '{op}'. Please choose +, -, *, or /.")

def main():
    print("📟 Welcome to the Python Calculator! (type 'exit' at any time to quit)\n")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        op   = get_operator()

        # ensure 'result' always exists
        result = None

        if op == '+':
            result = addition(num1, num2)
        elif op == '-':
            result = subtraction(num1, num2)
        elif op == '*':
            result = multiplication(num1, num2)
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is undefined.")
                continue
            result = division(num1, num2)

        # now safe to print
        print(f"\nResult: {num1} {op} {num2} = {result}\n")

        cont = input("Perform another calculation? (yes/no): ").strip().lower()
        if cont not in ('y', 'yes'):
            print("Thanks for using the calculator—goodbye!")
            break

if __name__ == "__main__":
    main()
