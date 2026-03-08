class Person:
    def __init__(self, name, student_id):
        self.__name = name  # 私有属性：姓名
        self.__student_id = student_id  # 私有属性：学号

    # 获取姓名
    def get_name(self):
        return self.__name

    # 获取学号
    def get_student_id(self):
        return self.__student_id

    # 修改姓名
    def set_name(self, new_name):
        self.__name = new_name

    # 修改学号
    def set_student_id(self, new_id):
        self.__student_id = new_id


class Course:
    """课程类：封装课程名、学分、成绩，实现封装"""
    def __init__(self, course_name, credit):
        self.__course_name = course_name  # 私有属性：课程名
        self.__credit = credit  # 私有属性：学分
        self.__score = 0.0  # 私有属性：成绩，初始化为0

    # 获取课程名
    def get_course_name(self):
        return self.__course_name

    # 获取学分
    def get_credit(self):
        return self.__credit

    # 获取成绩
    def get_score(self):
        return self.__score

    # 设置成绩（基础校验：0-100）
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩必须在0-100之间！")

    # 修改学分
    def set_credit(self, new_credit):
        if new_credit > 0:
            self.__credit = new_credit
        else:
            raise ValueError("学分必须为正数！")


class Student(Person):
    """子类：学生类，继承Person，新增课程列表、GPA属性"""
    def __init__(self, name, student_id, major):
        super().__init__(name, student_id)  # 调用父类构造方法
        self.__major = major  # 私有属性：专业
        self.__courses = []  # 私有属性：课程列表，存储Course实例
        self.__gpa = 0.0  # 私有属性：GPA，初始化为0

    # 获取专业
    def get_major(self):
        return self.__major

    # 获取课程列表
    def get_courses(self):
        return self.__courses

    # 获取GPA
    def get_gpa(self):
        return round(self.__gpa, 2)  # 保留2位小数

    # 设置GPA
    def set_gpa(self, gpa):
        self.__gpa = gpa

    # 添加课程
    def add_course(self, course):
        if isinstance(course, Course):
            self.__courses.append(course)
        else:
            raise TypeError("必须添加Course类的实例！")

    # 修改专业
    def set_major(self, new_major):
        self.__major = new_major