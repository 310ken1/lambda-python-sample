import pg8000.native


def hello(event, context):
    try:
        connect = pg8000.native.Connection(
            host="localhost",
            port="5432",
            database="testdb",
            user="postgres",
            password="postgres")
        prepare = connect.prepare("SELECT * FROM data WHERE id=:id;")
        results = prepare.run(id=1)
    except Exception:
        print("Connection failed")
    finally:
        print("Connection finally")
        prepare.close()
        connect.close()

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "data": results
    }
