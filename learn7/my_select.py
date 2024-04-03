from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Group, Teacher, Subject, engine

Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    query_result = (
        session.query(Student.name, func.avg(Grade.rating).label("avg_rating"))
        .join(Grade, Grade.student == Student.name)
        .group_by(Student.name)
        .order_by(func.avg(Grade.rating).desc())
        .limit(5)
        .all()
    )

    for student, avg_rating in query_result:
        print(f"Student: {student}, Average Rating: {avg_rating}")


def select_2():
    query_result = (
        session.query(Grade.student, func.avg(Grade.rating).label('avg_rating'))
        .group_by(Grade.student)
        .order_by(func.avg(Grade.rating).desc())
        .limit(1)
        .first()
    )

    print(*query_result)


def select_3():
    query_result = (
        session.query(
            Student.group_name, Subject.name, func.avg(Grade.rating).label("avg_rating")
        )
        .join(Grade, Student.name == Grade.student)
        .filter(Grade.subject == Subject.name, Subject.id == 3)
        .group_by(Student.group_name, Subject.name)
        .all()
    )

    for row in query_result:
        print(*row)


def select_4():
    query_result = session.query(func.avg(Grade.rating).label("avg_rating")).scalar()

    print(query_result)

def select_5():
    query_result = (
        session.query(Subject.name, Subject.teacher)
        .join(Teacher, Teacher.name == Subject.teacher)
        .filter(Teacher.id == 4)
        .all()
    )

    print(*query_result)


def select_6():
    query_result = (
        session.query(Student.name, Student.group_name)
        .join(Group, Group.name == Student.group_name)
        .filter(Group.id == 1)
        .all()
        )
    for row in query_result:
        print(row)


def select_7():
    query_result = (
        session.query(Grade.student, Student.group_name, Grade.subject, Grade.rating)
        .join(Student, Student.name == Grade.student)
        .join(Group, Student.group_name == Group.name)
        .join(Subject, Subject.name == Grade.subject)
        .filter(Group.id == 2, Subject.id == 3)
        .all()
    )

    for row in query_result:
        print(row)


def select_8():
    query_result = (
        session.query(
            Subject.teacher, Subject.name, func.avg(Grade.rating).label("avg_rating")
        )
        .join(Grade, Grade.subject == Subject.name)
        .filter(Subject.id == 3)
        .group_by(Subject.teacher, Subject.name)
        .all()
    )
    for row in query_result:
        print(row.teacher, row.name, row.avg_rating)

def select_9():
    query_result = (
        session.query(Student.name, Subject.name)
        .join(Grade, Grade.subject == Subject.name)
        .join(Student, Student.name == Grade.student)
        .group_by(Student.name, Subject.name)
        .filter(Grade.id == 4)
        .all()
    )

    for row in query_result:
        print(row)


def select_10():
    query_result = (
        session.query(Student.name, Subject.name, Subject.teacher)
        .join(Grade, Grade.subject == Subject.name)
        .join(Teacher, Subject.teacher == Teacher.name)
        .group_by(Student.name, Subject.name, Subject.teacher)
        .filter(Student.id == 1, Teacher.id == 2)
        .all()
    )

    for row in query_result:
        print(row)




select_10()
print("10-------------------------")
