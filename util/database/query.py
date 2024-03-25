from . import connect


def get_students() -> list[tuple[int, str]]:
    '''
    Contents of return : [(school_id, name)]
    '''
    conn = connect.get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT school_id, name FROM students;")
    students = cur.fetchall()
    
    cur.close()
    conn.close()
    return students

def get_homework() -> list[tuple[int, int, str, str]]:
    '''
    Contents of return : [(homework_id, subject, start_date, end_date)]
    '''
    conn = connect.get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT homework_id, subject, start_date, end_date FROM homeworks;")
    homeworks = cur.fetchall()
    
    cur.close()
    conn.close()
    return homeworks;


def get_submission(homework_id) -> list[list[str]]:
    '''
    Contents of return : [(school_id, name, submitted_or_not)]
    '''
    conn = connect.get_connection()
    cur = conn.cursor()
    submissions = []
    
    cur.execute(f"""SELECT s.school_id, s.name
                FROM students s
                WHERE NOT EXISTS (
                    SELECT 1    
                    FROM submissions sub
                    WHERE sub.school_id = s.school_id
                    AND sub.homework_id = {homework_id});""")
    for student in cur.fetchall():
        submissions.append([str(student[0]), student[1], "False"])
        
    cur.execute(f"""SELECT s.school_id, s.name
                FROM students s
                WHERE EXISTS (
                    SELECT 1    
                    FROM submissions sub
                    WHERE sub.school_id = s.school_id
                    AND sub.homework_id = {homework_id});""")

    for student in cur.fetchall():
        submissions.append([str(student[0]), student[1], "True"])
    
    return submissions
