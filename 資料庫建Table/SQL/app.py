import pymysql

def search_terms_with_like_and_match(keyword, db_config):
    query = f"""
    SELECT terms, related_term
    FROM searching
    WHERE MATCH(terms, related_term) AGAINST ('{keyword}' IN NATURAL LANGUAGE MODE)
      OR terms LIKE '%{keyword}%'
      OR related_term LIKE '%{keyword}%';
    """

    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    finally:
        connection.close()

# 測試
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'your_database'
}

keyword = 'input("請輸入要查詢的關鍵字: ")'
results = search_terms_with_like_and_match(keyword, db_config)

# 顯示結果
for term, related in results:
    print(f"Terms: {term}, Related: {related}")



