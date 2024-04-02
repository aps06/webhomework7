from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
import random

engine = create_engine("postgresql://postgres:1111@localhost/postgres", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def fill_data():

    groups = ['Group_1', 'Group_2', 'Group_3']
    for group_name in groups:
        group = Group(name=group_name)
        session.add(group)

    students = []
    for _ in range(30):
        student_name = Faker().name()
        students.append(student_name)
        group = random.choice(groups)
        student = Student(name=student_name, group_name=group)
        session.add(student)

    subjects = ["Mathematics",
                    "Physics",
                    "Chemistry",
                    "History",
                    "Literature"]

    for i in range(5):
        teacher_name = Faker().name()
        teacher = Teacher(name=teacher_name)
        session.add(teacher)

        subject = Subject(name=subjects[i], teacher=teacher_name)
        session.add(subject)

    for student_name in students:
        for subject_name in subjects:
            rating = random.randint(50, 100)
            date_received = Faker().date_between(start_date="-1y", end_date="today")
            grade = Grade(
                student=student_name,
                subject=subject_name,
                rating=rating,
                date_received=date_received,
            )
            session.add(grade)

    session.commit()


if __name__ == '__main__':
    fill_data()
