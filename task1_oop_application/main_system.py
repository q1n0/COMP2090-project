from entity import Student, Course
from calculator import GPACalculator

class GradeManagementSystem:
    """成绩管理主系统：提供学生/课程添加、成绩录入、GPA计算基础功能"""
    def __init__(self):
        self.__students = []  # 存储所有学生实例
        self.__gpa_calculator = GPACalculator()  # 实例化GPA计算器

    # 添加学生
    def add_student(self):
        print("\n===== 录入学生信息 =====")
        name = input("请输入学生姓名：")
        student_id = input("请输入学生学号：")
        major = input("请输入学生专业：")
        # 创建学生实例并添加到列表
        student = Student(name, student_id, major)
        self.__students.append(student)
        print(f"学生【{name}（{student_id}）】添加成功！")
        return student

    # 为学生添加课程并录入成绩
    def add_course_and_score(self, student):
        print(f"\n===== 为{student.get_name()}录入课程成绩 =====")
        course_num = int(input("请输入要录入的课程数量："))
        for i in range(course_num):
            print(f"\n--- 第{i+1}门课程 ---")
            course_name = input("课程名：")
            credit = float(input("学分（正数）："))
            score = float(input("成绩（0-100）："))
            # 创建课程实例并设置成绩
            course = Course(course_name, credit)
            course.set_score(score)
            # 为学生添加课程
            student.add_course(course)
            print(f"课程【{course_name}】录入成功！")

    # 计算学生GPA并展示
    def show_student_gpa(self, student):
        # 计算加权GPA
        gpa = self.__gpa_calculator.calculate_weighted_gpa(student)
        student.set_gpa(gpa)
        # 展示信息
        print("\n===== 学生GPA信息 =====")
        print(f"学号：{student.get_student_id()}")
        print(f"姓名：{student.get_name()}")
        print(f"专业：{student.get_major()}")
        print(f"总GPA（学分加权）：{student.get_gpa()}")
        # 展示各科成绩和绩点
        print("\n--- 各科成绩详情 ---")
        for course in student.get_courses():
            course_gpa = self.__gpa_calculator.score_to_gpa(course.get_score())
            print(f"{course.get_course_name()}（{course.get_credit()}学分）：{course.get_score()}分 → 绩点{course_gpa}")

    # 获取所有学生
    def get_all_students(self):
        return self.__students

# 主系统入口
if __name__ == "__main__":
    # 实例化主系统
    system = GradeManagementSystem()
    print("===== 学生成绩GPA管理系统（预提交版） =====")
    # 基础功能演示：添加1个学生+录入课程+计算GPA
    student = system.add_student()
    system.add_course_and_score(student)
    system.show_student_gpa(student)
    print("\n===== 演示完毕） =====")