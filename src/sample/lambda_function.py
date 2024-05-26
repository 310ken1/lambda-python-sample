"""Lambda関数(Amazon API Gateway)サンプル

- Python の Lambda 関数ハンドラー
  https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-handler.html

- Amazon API Gateway で AWS Lambda を使用する
  https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/services-apigateway.html#apigateway-example-event

- HTTP API の AWS Lambda プロキシ統合の使用
  https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html

"""

import random


def lambda_handler(event: dict, context: dict) -> dict:
    """Amazon API Gateway Lambdaサンプルハンドラ

    1から10までの値を、リクエストで指定したcount数レスポンスとして返す

    Args:
      event (dict): イベントオブジェクト
      context (dict): コンテキストオブジェクト
    Returns:
      dict: レスポンス
    """
    try:
        status_code: int = 200
        response_body: dict = {"answer1": [], "answer2": []}

        request = event["body"]
        count = request["count"]

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        response_body["answer1"] = random.sample(data, count)
        response_body["answer2"] = random.sample(data, count)

    except KeyError as e:
        status_code = 400
        response_body = {"message": "パラメータ異常"}
        print(f"error={repr(e)}")

    response: dict = {"statusCode": status_code, "body": response_body}
    print(f"response={response}")
    return response


if __name__ == "__main__":
    lambda_handler(event={"body": {"count": 2}}, context={})
