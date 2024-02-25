from connect import get_connection, DatabaseType


# 初始化数据库连接

def insert_submit(numbers) -> None:
    conn = get_connection(DatabaseType.SQLITE)
    cur = conn.cursor()

    for number in numbers:
        cur.execute(f"SELECT * FROM students WHERE id = {number};")
        ret = cur.fetchone()
        if ret is None:
            continue
        else:
            cur.execute(f"INSERT INTO submit VALUES ({number}, date());")
            print(f"Inserted {number} into submit table")
    

    conn.commit()
    conn.close()
