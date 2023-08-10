import csv
import json
import pandas as pd
import numpy as np

STUDENTS = 'People.json'


class Student:
    def __init__(self, sid, title, firstname, other_name, surname, city, age):
        self.sid = sid
        self.title = title
        self.firstname = firstname
        self.other_name = other_name
        self.surname = surname
        self.title = title
        self.city = city
        self.age = age

    def __repr__(self):
        string = (f'ID: {self.sid} '
                  + f'Title: {self.title} '
                  + f'Firstname: {self.firstname} '
                  + f'Other name: {self.other_name} '
                  + f'Surname: {self.surname} '
                  + f'Age: {self.age} '
                  + f'City: {self.city} ')
        return string

    def __iter__(self):
        return self


# read file
def read_student_file(file: str):
    try:
        with open(file) as json_file:
            data = json.load(json_file)
        return data

    except FileNotFoundError:
        print('No File found!')


# create generator holding students
def students_generator(data):
    for i in range(len(data['students'])):
        fullname = data['students'][i].get('fullName')
        student = Student(sid=data['students'][i].get('id'),
                          title=fullname.get('title'),
                          firstname=fullname.get('first'),
                          other_name=fullname.get('other')[0],
                          surname=fullname.get('surname'),
                          age=data['students'][i].get('age'),
                          city=data['students'][i].get('city'))

        yield student


# generator to list, list to dataframe
def write_to_csv(students_gen):
    students_list = []

    # iterate students generator
    for i, student in enumerate(students_gen):
        # dataframe format
        s = {'ID': student.sid,
             'Title': student.title,
             'Firstname': student.firstname,
             'Other name': student.other_name,
             'Surname': student.surname,
             'Age': student.age,
             'City': student.city}
        students_list.append(s)

    if len(students_list) > 0:
        df = pd.DataFrame(students_list)
        # save to csv
        df.to_csv('students.csv')



d = read_student_file(file=STUDENTS)
gen = students_generator(d)
write_to_csv(gen)