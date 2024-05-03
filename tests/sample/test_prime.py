import sys
import pytest
from prime import is_prime


@pytest.fixture
def before_and_after():
    print('BEFORE')
    yield
    print('AFTER')


def test_is_prime():
    """単項目テスト
    １項目のテストとして実施される
    """
    print("test_is_prime")
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)


@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
])
def test_is_prime_param(number, expected):
    """複数項目テスト
    パラメータ項目数テストとして実施される
    """
    print(sys._getframe().f_code.co_name)
    assert is_prime(number) == expected
