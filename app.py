import os
import pymysql

# ======================
# MySQL 数据库连接设置
# ======================
def get_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl={'ssl': {}}  # Aiven 数据库需要 SSL
    )
    return connection

# ======================
# 启动时测试数据库连接
# ======================
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Successfully connected to Aiven MySQL!")
        conn.close()
    except Exception as e:
        print("❌ Database connection failed:", e)
