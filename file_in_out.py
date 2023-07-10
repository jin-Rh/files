import json
import pandas as pd


class Student:
    def __init__(self, sid, title, firstname, othername, surname, city, age):
        self.title = title
        self.firstname = firstname
        self.othername = othername
        self.surname = surname
        self.title = title
        self.sid = sid
        self.city = city
        self.age = age

    def __repr__(self):
        string = (f'ID: {self.sid} '
                  + f'Title: {self.title} '
                  + f'Firstname: {self.firstname} '
                  + f'Othername: {self.othername} '
                  + f'Surname: {self.surname} '
                  + f'Age: {self.age} '
                  + f'City: {self.city} ')
        return string


# read file using class
def translate_file(file: str):
    """
    This function take a json file and parse, generate a csv file.
    file: input json file

    """

    students_in = []
    students_out = []

    with open(file) as json_file:
        data = json.load(json_file)

    # reading from json
    for i in range(len(data['students'])):
        fullname = data['students'][i].get('fullName')
        student = Student(sid=data['students'][i].get('id'),
                          title=fullname.get('title'),
                          firstname=fullname.get('first'),
                          othername=fullname.get('other')[0],
                          surname=fullname.get('surname'),
                          age=data['students'][i].get('age'),
                          city=data['students'][i].get('city'))

        students_in.append(student)

    print(students_in)

    # writing to dataframe and save to csv
    if len(students_in) > 0:
        for student in students_in:
            a = {'ID': student.sid,
                 'Title': student.title,
                 'Firstname': student.firstname,
                 'Other name': student.othername,
                 'Surname': student.surname,
                 'Age': student.age,
                 'City': student.city}
            students_out.append(a)

        df = pd.DataFrame(students_out)
        # save to csv
        df.to_csv('student_file.csv')
    else:
        print('No data to save')
