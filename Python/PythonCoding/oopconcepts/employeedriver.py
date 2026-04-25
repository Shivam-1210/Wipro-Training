from oopconcepts.employeedetails import EmployeeDetails

# driver
eno = int(input('Emp no: '))
name = (input('Emp name: '))
bp = float(input('Basic pay: '))

employee = EmployeeDetails(empno = eno, ename = name, basicpay = bp)

print('Emp no: ',employee.get_empno())
print('Emp name: ',employee.ename)
print('Basic pay: ',employee.basic_pay)
print('Salary: ',employee.calculate_net_sal())

