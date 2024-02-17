import connect


# 初始化数据库连接

def insert_submit(numbers) -> None:
    cur = connect.connect_to_db()

    for number in numbers:
        cur.execute(f"SELECT * FROM students WHERE id = {number};")
        ret = cur.fetchone()
        if ret is None:
            continue
        else:
            cur.execute(f"INSERT INTO submit VALUES ({number}, date());")
            print(f"Inserted {number} into submit table")
