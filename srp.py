# SRP(Single Responsibility Principle)
# 클래스는 단 한개의 책임
"""
분리 필요
"""
class StudentScoreAndCourseManager(object):
    def __init__(self):
        scores = {}
        courses = {}
        
    def get_score(self, student_name, course):
        pass
    
    def get_courses(self, student_name):
        pass

"""
score와 course 분리

"""
class ScoreManager(object):
    def __init__(self):
        scores = {}
        
    def get_score(self, student_name, course):
        pass
    
    
class CourseManager(object):
    def __init__(self):
        courses = {}
    
    def get_courses(self, student_name):
        pass