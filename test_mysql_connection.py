import pymysql

DB_CONFIG = {
    "host": "mysql-2dba6397-kouhanren-deployment.h.aivencloud.com",
    "port": 13545,
    "user": "avnadmin",
    "password": "AVNS_aQX2oxh9n81Sc_W2o68",
    "database": "defaultdb",
    "ssl": {"ssl": {}}   # Aiven 必须使用 SSL
}

connection = None  # 提前定义

try:
    connection = pymysql.connect(**DB_CONFIG)
    print("✅ Successfully connected to Aiven MySQL cloud database!")
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("📂 Current tables:", tables)
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    if connection:  # 只有在连接创建成功时才关闭
        connection.close()
