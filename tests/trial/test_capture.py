def fibonacci(n: int):
    a = 0
    b = 1

    for _ in range(n):
        print(b)

        a, b = b, a + b


def test_fibonacci(capsys):
    fibonacci(5)

    stdout, stderr = capsys.readouterr()
    print(stdout)

    assert stdout == (
        '1\n'
        '1\n'
        '2\n'
        '3\n'
        '5\n'
    )
