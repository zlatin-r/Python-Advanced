def math_operations(expression):
    num1, sign, num2 = expression.split()
    result = 0

    if sign == "/":
        result = float(num1) / int(num2)
    elif sign == "*":
        result = float(num1) * int(num2)
    elif sign == "-":
        result = float(num1) - int(num2)
    elif sign == "+":
        result = float(num1) + int(num2)
    elif sign == "^":
        result = float(num1) ** int(num2)

    return print(f"{result:.2f}")
