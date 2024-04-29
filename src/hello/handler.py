import pg8000.native
import boto3
import json


def get_parameter(key):
    """Get parameter from SSM
    Args:
        key (str): Parameter key
    Returns:
        dict: Parameter value
    """
    ssm = boto3.client('ssm')
    param = ssm.get_parameter(Name=key)
    return json.loads(param['Parameter']['Value'])


def hello(event, context):
    try:
        settings = get_parameter('Test')
        connect = pg8000.native.Connection(
            host=settings['db']['host'],
            port=settings['db']['port'],
            database=settings['db']['database'],
            user=settings['db']['user'],
            password=settings['db']['password'])
        prepare = connect.prepare("SELECT * FROM data WHERE id=:id;")
        results = prepare.run(id=1)
    except Exception as e:
        print(f"Unexpected {e=}, {type(e)=}")
    finally:
        print("Connection finally")
        prepare.close()
        connect.close()

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "data": results
    }
