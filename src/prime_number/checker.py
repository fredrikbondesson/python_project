import argparse
import sys
from typing import List, NamedTuple


class PrimeNumber(NamedTuple):
    number: int
    is_prime: bool


def is_prime(num) -> bool:
    if num in [0, 1]:
        return False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False

    return True


def check_numbers(numbers: List[int]) -> List[PrimeNumber]:
    result = []
    for number in numbers:

        if is_prime(number):
            flag = "is"
            res = PrimeNumber(number, True)
        else:
            flag = "is not"
            res = PrimeNumber(number, False)

        result.append(res)
        print("%d %s a prime number." % (number, flag))

    return result


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
