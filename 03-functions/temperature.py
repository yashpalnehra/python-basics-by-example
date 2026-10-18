def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def describe(celsius):
    if celsius <= 0:
        return "freezing"
    if celsius < 15:
        return "cold"
    if celsius < 25:
        return "mild"
    return "hot"


def main():
    print(f"{'C':>6} {'F':>6}  feels")
    for c in range(-10, 41, 10):
        f = celsius_to_fahrenheit(c)
        print(f"{c:>6} {f:>6.1f}  {describe(c)}")


if __name__ == "__main__":
    main()
