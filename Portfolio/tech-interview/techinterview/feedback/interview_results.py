from questions.models import Questions
from departments.models import Departments
from interviews.models import Interviews
from feedback.models import Comments, Grades
from functools import reduce


class InterviewResults:
    __expert_levels = ['Junior', 'Middle', 'Senior', 'Lead']
    grades = Grades.objects.all()

    def __init__(self, interview_id):
        self.interview_id = interview_id
        __interview = Interviews.objects.get(id=interview_id)
        self.__questions = Departments.objects.get(
            id=__interview.f_department_id).questions.all()
        self.__comments = Comments.objects.filter(f_interview=__interview)

    @property
    def levels(self):
        levels = {}
        for question, comment in zip(self.__questions, self.__comments):
            levels[question.id] = self.__expert_levels[self.grades.get(id=comment.f_grade_id).weight]
        return levels

    @property
    def total(self):
        return self.__expert_levels[round(reduce(lambda x, y: x+y,
                            [self.grades.get(id=comment.f_grade_id).weight for comment in self.__comments])
                     / len(self.__comments))]
