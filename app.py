import os
import pymysql
from bottle import Bottle, response

app = Bottle()

@app.route("/test-db")
def test_db():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            ssl={'ssl': {}}
        )
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            tables = [row[0] for row in cursor.fetchall()]
        connection.close()

        response.content_type = "application/json"
        return {"status": "✅ connected", "tables": tables}

    except Exception as e:
        response.content_type = "application/json"
        return {"status": "❌ failed", "error": str(e)}


# Render 平台要求显式绑定 0.0.0.0 和端口号
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
