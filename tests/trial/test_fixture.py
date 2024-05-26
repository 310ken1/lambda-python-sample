import sys
import pytest


"""
printの出力を表示するには-sオプションをつけて実行する
pytest -s test_fixture.py
"""


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print(f'↓↓前処理↓↓ {sys._getframe().f_code.co_name}')
    yield f'戻り値({sys._getframe().f_code.co_name})'
    print(f'↑↑後処理↑↑ {sys._getframe().f_code.co_name}')


@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print(f'↓↓前処理↓↓ {sys._getframe().f_code.co_name}')
    yield f'戻り値({sys._getframe().f_code.co_name})'
    print(f'↑↑後処理↑↑ {sys._getframe().f_code.co_name}')


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print()
    print(f'↓↓前処理↓↓ {sys._getframe().f_code.co_name}')
    yield f'戻り値({sys._getframe().f_code.co_name})'
    print(f'↑↑後処理↑↑ {sys._getframe().f_code.co_name}')


@pytest.fixture(scope='function')
def function_fixture():
    print(f'↓↓前処理↓↓ {sys._getframe().f_code.co_name}')
    yield f'戻り値({sys._getframe().f_code.co_name})'
    print(f'↑↑後処理↑↑ {sys._getframe().f_code.co_name}')


def test_fixture1():
    print(sys._getframe().f_code.co_name)


def test_fixture2(function_fixture):
    print(sys._getframe().f_code.co_name)
    print(f'  {function_fixture}')


def test_fixture3():
    print(sys._getframe().f_code.co_name)
