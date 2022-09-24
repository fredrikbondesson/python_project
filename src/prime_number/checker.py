import argparse
import sys
from typing import List


def is_prime(nr) -> bool:
    if nr <= 3:
        return nr > 1

    if nr % 2 == 0 or nr % 3 == 0:
        return False

    sqrt = int(nr**0.5) + 1

    for divisor in range(5, sqrt, 2):
        if nr % divisor == 0:
            return False

    return True


def check_numbers(numbers: List[int]) -> None:
    for number in numbers:
        if is_prime(number):
            flag = "is"
        else:
            flag = "is not"
        print("%d %s a prime number." % (number, flag))


def main(args):
    parser = argparse.ArgumentParser(
        "Check if specified numbers are prime numbers or not."
    )

    parser.add_argument(
        "numbers",
        metavar="N",
        type=int,
        nargs="+",
        help="""The numbers to check, separated by empty space.""",
    )

    arguments = parser.parse_args(args=args)
    numbers = arguments.numbers
    print(f"numbers={numbers}")
    check_numbers(numbers)


if __name__ == "__main__":
    main(sys.argv[1:])
