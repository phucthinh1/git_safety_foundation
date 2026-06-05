def add(a, b):
    return a + b


def subtract(a, b):
    return a - b



def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(expression):
    try:
        return eval(expression, {"__builtins__": None}, {
            "add": add,
            "subtract": subtract,
            "divide": divide
        })
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def main():
    print("Basic calculator")
    print("Enter expressions using +, -, *, / or functions add(), subtract(), multiply(), divide()")
    while True:
        try:
            expr = input("> ").strip()
            if not expr:
                continue
            if expr.lower() in {"exit", "quit"}:
                break
            result = calculate(expr)
            print(result)
        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()