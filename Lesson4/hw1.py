"""
Create classes to track homeworks.

1. Homework - accepts homework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""
from datetime import datetime, timedelta


class DeadlineError(Exception):
    pass


class ReadyHomework:
    def __init__(self, student, homework, solution):
        self.author = student
        self.solution = solution
        self.name = homework


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.now() + timedelta(days=deadline)

    def is_deadline_passed(self):
        return self.deadline < datetime.now()


class Student:
    def __init__(self, second_name, first_name):
        self.second_name = second_name
        self.first_name = first_name

    def do_homework(self, homework, solution):
        if homework.is_deadline_passed():
            raise DeadlineError("You are late")
        else:
            ready_homework = ReadyHomework(self, homework, solution)
            return ready_homework


class Teacher:
    homework_done = {}

    def __init__(self, t_second_name, t_first_name):
        self.t_second_name = t_second_name
        self.t_first_name = t_first_name

    @classmethod
    def create_homework(cls, text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, task):
        Teacher.homework_done[task.name] = []
        if len(task.solution) > 5:
            Teacher.homework_done[task.name].append(task)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, *task):
        if len(task) == 0:
            Teacher.homework_done = {}
        else:
            del Teacher.homework_done[task]
