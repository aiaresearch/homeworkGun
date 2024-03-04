import os

def clear_database():
    os.remove(os.path.join(os.path.join(os.path.dirname(__file__), '..'), 'homework.db'))
    # print(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '/homework.db'))


if __name__ == '__main__':
    clear_database()