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
        .filter(Grade.subject == 'Physics')
        .group_by(Grade.student)
        .order_by(func.avg(Grade.rating).desc())
        .limit(1)
        .first()
    )

    print(*query_result)


def select_3():
    query_result = (
        session.query(Group.name, Grade.subject, func.avg(Grade.rating).label("avg_rating"))
        .join(Student, Student.group_name == Group.name)
        .join(Grade, Grade.student == Student.name)
        .filter(Grade.subject == 'History')
        .group_by(Group.name, Grade.subject)
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
        .filter(Teacher.name == "Tracey Jenkins")
        .all()
    )

    print(*query_result)


def select_6():
    query_result = (
        session.query(Student.name, Student.group_name)
        .join(Group, Group.name == Student.group_name)
        .filter(Student.group_name == 'Group_1')
        .all()
        )
    for row in query_result:
        print(row)


def select_7():
    query_result = (
        session.query(Grade.student, Student.group_name, Grade.subject, Grade.rating)
        .join(Student, Student.name == Grade.student)
        .filter(Student.group_name == "Group_2", Grade.subject == "Chemistry")
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
        .filter(Subject.teacher == "David Aguilar")
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
        .filter(Grade.student == "Timothy Johnson")
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
        .filter(Student.name == "Haley Hoffman", Teacher.name == "Tracey Jenkins")
        .all()
    )

    for row in query_result:
        print(row)

select_10()
