import sys


class CalcError(Exception):
    pass


def parse(expression):
    parts = expression.split()
    if len(parts) != 3:
        raise CalcError("expected NUMBER OPERATOR NUMBER, like 3 + 4")
    left, op, right = parts
    try:
        return float(left), op, float(right)
    except ValueError:
        # our message is enough, drop the float() traceback
        raise CalcError(f"not a number: {left} or {right}") from None


def calculate(expression):
    left, op, right = parse(expression)
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        if right == 0:
            raise CalcError("cannot divide by zero")
        return left / right
    raise CalcError(f"unknown operator: {op}")


def main():
    expression = " ".join(sys.argv[1:])
    if not expression:
        print("usage: calculator.py NUMBER OPERATOR NUMBER")
        sys.exit(1)
    try:
        print(calculate(expression))
    except CalcError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
