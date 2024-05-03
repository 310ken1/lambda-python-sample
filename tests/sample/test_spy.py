import test_spy

"""
動作させるために以下が必要
pipenv install -d pytest-mock
"""


def send(message: str):
    """テスト対象"""
    return receive(message)


def receive(message: str) -> bool:
    """モック対象"""
    print('received: {}'.format(message))
    return False


def test_send(mocker):
    """テストコード"""
    # 引数していした関数がスパイ化される
    # receiveにassert_called_once_withのメソッドが追加される
    receive = mocker.spy(test_spy, 'receive')

    result = send('Hello World!')

    assert not result

    # 一度だけコールされたことの確認
    receive.assert_called_once_with('Hello World!')

    # 呼び出し履歴を確認
    assert receive.call_args_list == [
        mocker.call('Hello World!'),
    ]
