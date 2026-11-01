import json
import os

class StudentRecordError(Exception):
    pass

def read_students():
    filename="student_input.json"

    with open(filename,"r",encoding="utf-8")as file:
        students=json.load(file)
        print("Json file read successfully")
        for student in students:
            return students
        print ("file reading operation completed")

students=read_students()        