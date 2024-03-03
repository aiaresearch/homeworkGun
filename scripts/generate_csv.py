import os
import random
import csv

# 定义一个函数，用于生成随机学号
def generate_student_id():
    return str(random.randint(1000, 9999))

# 定义一个函数，用于生成随机名称
def generate_student_name():
    first_names = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王"]
    last_names = ["伟", "芳", "娜", "强", "磊", "军", "洋", "勇", "艳", "杰"]
    return random.choice(first_names) + random.choice(last_names)

number_of_students = 10


students = []

for _ in range(number_of_students):
    student_id = generate_student_id()
    student_name = generate_student_name()
    students.append([student_id, student_name])

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(script_dir, "students.csv")

with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print(f"Successfully generated {number_of_students} random students and saved to '{csv_file_path}' file.")
