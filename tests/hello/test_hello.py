import boto3

from src.hello.handler import get_parameter
from moto import mock_aws


@mock_aws
def test_get_arameter():
    ssm = boto3.client('ssm')
    ssm.put_parameter(
        Name='Test', Value="""
        {
            "db": {
                "host": "localhost",
                "port": "5432",
                "database": "testdb",
                "user": "postgres",
                "password": "postgres"
            }
        }
        """, Type='String')

    result = get_parameter('Test')

    assert result['db']['host'] == 'localhost'
    assert result['db']['port'] == '5432'
    assert result['db']['database'] == 'testdb'
    assert result['db']['user'] == 'postgres'
    assert result['db']['password'] == 'postgres'
