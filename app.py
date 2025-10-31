import os
import pymysql
from flask import Flask, jsonify  # 如果你是 Bottle，我也可以帮你改成 Bottle 版本

app = Flask(__name__)

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
        return jsonify({"status": "✅ connected", "tables": tables})
    except Exception as e:
        return jsonify({"status": "❌ failed", "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
