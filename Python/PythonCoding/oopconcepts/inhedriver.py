from oopconcepts.college import College
from oopconcepts.student import Student
from oopconcepts.studentgrade import StudentGrade
from oopconcepts.teacher import Teacher

cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('C City :')
rno = int(input('Roll No: '))
sn = input('Stu Name: ')
m1 = int(input('M1: '))
m2 = int(input('M2: '))
m3 = int(input('M3: '))
eid = int(input('Eid: '))
tn = input('Teacher Name: ')
de  = input('Dept name: ')
bp = float(input('Bp: '))

'''project.display_college_details()
project = College(ccode=cc, cname=cn, ccity=ci)

project.welcome_message()'''

project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno= rno, sname=sn, m1=m1, m2=m2, m3=m3)

project.welcome_message()
project.display_college_details()
print(f'Roll No: {project.rollno} \nName: {project.stuname} \nTotal: {project.calculate_total()} \nAverage: {project.calculate_average()}')
project.calculate_grade()
project.calculate_result()
print(f'Result: {project.result} \t Grade: {project.grade}')


teach =  Teacher(ccode = cc, cname = cn, ccity = ci, eid = eid, tn = tn, bp = bp, de = de)
print(f'Eid: {teach.empid} \tName: {teach.tname} \tDept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')
