class GPACalculator:
    """GPA计算器"""
    GPA_RULE = {
        (90, 101): 4.0,
        (80, 90): 3.0,
        (70, 80): 2.0,
        (60, 70): 1.0,
        (0, 60): 0.0
    }

    @staticmethod
    def score_to_gpa(score):
        """静态方法：百分制成绩转绩点，无需实例化"""
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间！")
        # 匹配绩点规则
        for (low, high), gpa in GPACalculator.GPA_RULE.items():
            if low <= score < high:
                return gpa
        return 0.0

    def calculate_weighted_gpa(self, student):
        """实例方法：计算学分加权GPA，传入Student实例"""
        total_credit = 0.0  # 总学分
        total_gpa_credit = 0.0  # 总（绩点×学分）
        # 遍历学生的所有课程
        for course in student.get_courses():
            credit = course.get_credit()
            score = course.get_score()
            gpa = self.score_to_gpa(score)
            total_credit += credit
            total_gpa_credit += gpa * credit
        # 避免除零错误（无课程时GPA为0）
        if total_credit == 0:
            return 0.0
        # 计算学分加权GPA
        weighted_gpa = total_gpa_credit / total_credit
        return round(weighted_gpa, 2)