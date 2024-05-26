"""Lambda関数(Amazon API Gateway)サンプルテスト
"""

import os
import sys
from unittest.mock import call

import pytest

"""モジュール検索パス(Module Search Path)設定"""
paths = ["../../src/sample"]
for path in paths:
    sys.path.append(os.path.join(os.path.dirname(__file__), path))


params = {
    "正常 count=1": [
        # event"
        {"body": {"count": 1}},
        # context
        {"side_effect": [[1], [2]]},
        # expected
        {
            "response": {
                "statusCode": 200,
                "body": {"answer1": [1], "answer2": [2]},
            },
            "call_args_list": [
                call([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
                call([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
            ],
            "exception": None,
        },
    ],
    "正常 count=2": [
        # event"
        {"body": {"count": 2}},
        # context
        {"side_effect": [[1, 2], [3, 4]]},
        # expected
        {
            "response": {
                "statusCode": 200,
                "body": {"answer1": [1, 2], "answer2": [3, 4]},
            },
            "call_args_list": [
                call([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
                call([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            ],
        },
    ],
    "異常 count指定なし": [
        # event"
        {"body": {}},
        # context
        {"side_effect": [[1, 2], [3, 4]]},
        # expected
        {
            "response": {
                "statusCode": 400,
                "body": {"message": "パラメータ異常"},
            },
            "call_args_list": [],
        },
    ],
}


@pytest.mark.parametrize(
    "event, context, expected", list(params.values()), ids=list(params.keys())
)
def test_lambda_handler(mocker, event, context, expected):
    # モック設定
    # 戻り値を複数返す場合は、side_effectを利用し、
    # １つ返す場合は、return_valueを利用する
    sample = mocker.patch("random.sample", side_effect=context["side_effect"])

    # Lambda関数はimportすると初期化フェーズが実行されるため
    # モック設定した後にimportする
    import lambda_function

    # Lambda関数の実行
    response = lambda_function.lambda_handler(event, context)
    assert response == expected["response"]
    assert sample.call_args_list == expected["call_args_list"]
