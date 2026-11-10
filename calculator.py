"""A simple calculator."""


def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("cannot divide by zero")
        return a / b
    raise ValueError(f"unknown operator {op}")


if __name__ == "__main__":
    a = float(input("first number: "))
    op = input("operator (+ - * /): ")
    b = float(input("second number: "))
    print(calculate(a, op, b))
