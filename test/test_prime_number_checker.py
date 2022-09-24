from typing import List

import pytest

from prime_number import checker


def test_main():
    checker.main(["1", "2"])


def test_check_single_number():
    res = checker.check_numbers([1])
    assert len(res) == 1
    assert not res[0].is_prime
    assert res[0].number == 1


def test_multiple_single_number():
    res: List[checker.PrimeNumber] = checker.check_numbers([2, 3, 4, 5])
    assert len(res) == 4

    assert res[0].is_prime
    assert res[0].number == 2

    assert res[1].is_prime
    assert res[1].number == 3

    assert not res[2].is_prime
    assert res[2].number == 4

    assert res[3].is_prime
    assert res[3].number == 5


@pytest.mark.parametrize(
    "number, exp_result",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (22, False),
        (29, True),
        (81, False),
        (83, True),
    ],
)
def test_is_prime(number: int, exp_result: bool):
    assert checker.is_prime(number) == exp_result, (
        f"{number} should be prime number"
        if exp_result
        else f"{number} should NOT be prime number"
    )
