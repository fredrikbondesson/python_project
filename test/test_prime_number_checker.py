import pytest

from prime_number import checker


def test_check_numbers():
    pass


@pytest.mark.parametrize(
    "number, exp_result",
    [(1, False), (2, True), (3, True), (4, False), (5, True), (6, False)],
)
def test_is_prime(number: int, exp_result: bool):
    assert checker.is_prime(number) == exp_result, (
        f"{number} should be prime number"
        if exp_result
        else f"{number} should NOT be prime number"
    )
