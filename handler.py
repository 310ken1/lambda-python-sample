import pg8000.dbapi


def hello(event, context):
    try:
        con = pg8000.dbapi.connect(user="postgres", password="postgres",
                                   host="localhost", database="testdb")
        cur = con.cursor()
        cur.execute('SELECT to_json(data) FROM data;')
        results = cur.fetchall()
        cur.close()
    except Exception:
        print("Connection failed")
    finally:
        print("Connection successful")
        con.close()

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "data": results
    }
