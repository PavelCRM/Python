import csv
import os


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name
    
    def __set__(self, instance, value):
        if not value.replace(' ', '').isalpha() or not value.istitle():
            raise ValueError("Неверный формат имени")
        instance._name = value

class Student:
    name = NameDescriptor()

    def __init__(self, subjects_file, scores_file, test_results_file):
        self.subjects = self._load_subjects(subjects_file)
        self.scores = {subject: {'grades': [], 'test_results': []} for subject in self.subjects}
        self._load_scores(scores_file)
        self._load_test_results(test_results_file)

    def _load_subjects(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def _load_scores(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers
            for row in reader:
                subject = row[0]
                grade = int(row[1])
                if subject not in self.subjects:
                    raise ValueError("Invalid subject")
                if grade < 2 or grade > 5:
                    raise ValueError("Invalid grade")
                self.scores[subject]['grades'].append(grade)

    def _load_test_results(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers
            for row in reader:
                subject = row[0]
                result = int(row[1])
                if subject not in self.subjects:
                    raise ValueError("Invalid subject")
                if result < 0 or result > 100:
                    raise ValueError("Invalid test result")
                self.scores[subject]['test_results'].append(result)

    def get_average_grade(self, subject):
        if subject not in self.subjects:
            raise ValueError("Invalid subject")
        grades = self.scores[subject]['grades']
        if not grades:
            return 0
        return sum(grades) / len(grades)

    def get_average_test_result(self, subject):
        if subject not in self.subjects:
            raise ValueError("Invalid subject")
        test_results = self.scores[subject]['test_results']
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)

    def get_overall_average(self):
        total_grades = []
        total_test_results = []
        for subject in self.subjects:
            total_grades.extend(self.scores[subject]['grades'])
            total_test_results.extend(self.scores[subject]['test_results'])
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)

current_dir = os.path.dirname(os.path.abspath(__file__))
subjects_file = os.path.join(current_dir, 'subjects.csv')
scores_file = os.path.join(current_dir, 'scores.csv')
test_results_file = os.path.join(current_dir, 'test_results.csv')
student = Student(subjects_file, scores_file, test_results_file)
student.name = 'Николай Сергеевич Лавренец'

for subject in student.subjects:
    grade_avg = student.get_average_grade(subject)
    test_result_avg = student.get_average_test_result(subject)
    print(f"Student: {student.name}")
    print(f"Subject: {subject}, Average Grade: {grade_avg}, Average Test Result: {test_result_avg}")
    print()
