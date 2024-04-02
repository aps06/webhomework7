from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.engine import create_engine

engine = create_engine("postgresql://postgres:1111@localhost/postgres", echo=True)


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    group_name = Column(String(250), ForeignKey("groups.name"), nullable=False)
    groups = relationship("Group")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    teacher = Column(String(250), ForeignKey("teachers.name"))
    teachers = relationship("Teacher")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student = Column(String(250), ForeignKey("students.name"))
    subject = Column(String(250), ForeignKey("subjects.name"))
    rating = Column(Integer, nullable=False)
    date_received = Column(Date, nullable=False)
    students = relationship("Student")
    subjects = relationship("Subject")


Base.metadata.create_all(engine)
Base.metadata.bind = engine
