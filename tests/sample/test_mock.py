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
    # 引数していした関数がモック化される
    # return_valueで戻り値を変更可能
    receive = mocker.patch('test_mock.receive', return_value=True)

    result = send('Hello World!')

    assert True is result

    # 一度だけコールされたことの確認
    receive.assert_called_once_with('Hello World!')

    # 呼び出し履歴を確認
    assert receive.call_args_list == [
        mocker.call('Hello World!'),
    ]
