# import pymysql

# # 連接到 MySQL 資料庫
# try:
#     connection = pymysql.connect(
#         host='127.0.0.1:3306',       # 主機名
#         user='root',   # 使用者名稱
#         password='Hasay2612', # 密碼
#         database='FinVisionAI' # 資料庫名稱
#     )

#     print("成功連接到 MySQL 資料庫")

#     # 建立游標
#     cursor = connection.cursor()
#     cursor.execute("SELECT DATABASE();")
#     record = cursor.fetchone()
#     print("目前的資料庫是:", record)

# except pymysql.MySQLError as e:
#     print("連接失敗，錯誤如下:", e)

# finally:
#     connection.close()
#     print("MySQL 連接已關閉")


import pymysql

# 預設 connection 為 None
connection = None

try:
    # 嘗試連接到 MySQL 資料庫
    connection = pymysql.connect(
        host='localhost',       # 主機名
        user='root',   # 使用者名稱
        password='Hasay2612', # 密碼
        database='demo' # 資料庫名稱
    )

    print("成功連接到 MySQL 資料庫")

    # 執行查詢
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    record = cursor.fetchone()
    print("目前的資料庫是:", record)

except pymysql.MySQLError as e:
    print("連接失敗，錯誤如下:", e)

finally:
    # 確認 connection 已初始化
    if connection is not None:
        connection.close()
        print("MySQL 連接已關閉")