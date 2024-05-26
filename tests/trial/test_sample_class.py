import sample_class


class Dummy:
    def __init__(self) -> None:
        print("Dummy")

    def func1(self, arg1, arg2) -> bool:
        print(f"Dummy arg1={arg1} arg2={arg2}")
        return True


def test_sample_class(mocker):

    mocker.patch("sample_class.SampleClass", Dummy)
    c = sample_class.SampleClass()
    c.func1("1", "2")
