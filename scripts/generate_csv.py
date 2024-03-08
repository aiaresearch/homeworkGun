import os
import random
import csv

# 定义一个函数，用于生成随机学号
def generate_student_id():
    return str(random.randint(1000, 9999))

# 定义一个函数，用于生成随机名称
def generate_student_name():
    surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元']
    names = ['明', '芳', '华', '强', '军', '文', '丽', '静', '杰', '刚', '秀英', '勇', '敏', '飞', '霞', '超', '磊', '娜', '涛', '婷', '鹏', '洁', '鑫', '倩', '宇', '艳', '伟', '娟', '骏', '琳', '阳', '佳', '宁', '浩', '莹', '龙', '丹', '健', '蕾', '明', '莉', '亮', '玲', '刘', '涵', '志', '慧', '峰', '秀兰', '云', '波', '青', '杨', '燕', '松', '瑜', '丽华', '峰', '玉', '新', '梅', '海', '瑞', '梦', '春', '琴', '国', '翔', '桂英', '济', '雪', '弘', '彬', '彦', '亦', '靖', '鸿', '炜', '晓', '茜', '宝', '贵', '星', '光', '俊', '心', '丽', '民', '雄']

    surname = random.choice(surnames)  # 随机选择一个姓氏
    name = random.choice(names)        # 随机选择一个名字

    return f"{surname}{name}"

def generate_student():
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
