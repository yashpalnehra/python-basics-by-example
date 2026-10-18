import sys


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# upper limit from the command line, 100 if none given
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100

for i in range(1, limit + 1):
    print(fizzbuzz(i))
