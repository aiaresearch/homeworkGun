from . import connect


def get_homework() -> list[tuple]:
    conn = connect.get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT homework_id, subject, start_date, end_date FROM homeworks;")
    homeworks = cur.fetchall()
    
    cur.close()
    conn.close()
    return homeworks