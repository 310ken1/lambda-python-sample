import os
import sys
from unittest.mock import MagicMock


paths = [
    "../../src/sample"
]
current = os.path.dirname(os.path.abspath(__file__))
for path in paths:
    sys.path.append(os.path.join(current, path))

import sample_func
import sample_class

#sample_class.SampleClass.func1 = MagicMock()
sample_class.SampleClass = MagicMock()


class Dummy:
    def __init__(self) -> None:
        print("Dummy")

    def func1(self, arg1, arg2) -> bool:
        print(f"Dummy arg1={arg1} arg2={arg2}")
        return True


def test_sample_func(mocker):
    """
    func = mocker.patch("sample_class.SampleClass.func1")
    sample_func.sample_func()

    assert func.call_args_list == [
        mocker.call("3", "4")
    ]
    """
    print(sample_class.SampleClass)
    print(sample_func.sample_func())
    print(sample_class.SampleClass.return_value.func1.call_args_list)


