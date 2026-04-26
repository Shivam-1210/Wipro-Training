'''
list1 = input('Enter the numbers separated by spaces: ').split()
list1 = [int(num) for num in list1]

if list1:
    smallest = min(list1)
    largest = max(list1)
    print(f'smallest number: {smallest}')
    print(f'largest number: {largest}')

str1 = input('Enter a string: ')
print(len(str1))

names = input('Enter the list of names: ').split()
names.sort()
print(f'list in alphabetical order: {names}')

numbers  = input('Enter list of number separated by space: ').split()
numbers = [int(num) for num in numbers ]
total = 0
for i in numbers:
    total+=i
print(total)

str2 = input('Enter a string: ')
print(str2.upper())'''


'''def factorial(n):
    fact = 1
    while n>1:
        fact*=n
        n-=1
    return fact

num1 = int(input('Enter a number: '))
print(f'factorial of {num1} is: {factorial(num1)}')'''



'''def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = find_largest(num1, num2, num3)
print(f'The largest of {num1}, {num2}, and {num3} is {largest}')'''



'''def greet(name):
    print(f"Hello, {name}!")


user_name = input("Enter your name: ")
greet(user_name)'''

'''
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


num1_list = [10, 20, 30, 40, 50] 
avg = average(num1_list)
print(f'The average of {num1_list} is {avg}')'''


'''def is_palindrome(st):
    st.lower()
    return st == st[::-1]


t_string = ['radar', 'hello', 'level', 'world', 'aman asa nama']

for str in t_string:
    if is_palindrome(str):
        print(f'{str}: is a palindrome.')
    else:
        print(f'{str}: is not a palindrome.')'''

'''
import math

num = float(input('Enter a number to find its square root: '))
sqrt_num = math.sqrt(num)
print(f'The square root of {num} is {sqrt_num}')

angle = float(input('Enter an angle in degrees to find its sine: '))
angle_rad = math.radians(angle)
sine_val = math.sin(angle_rad)
print(f"The sine of {angle} is {sine_val}")


num1 = int(input('Enter the first number for GCD: '))
num2 = int(input('Enter the second number for GCD: '))
gcd_val = math.gcd(num1, num2)
print(f'The GCD of {num1} and {num2} is {gcd_val}')'''

'''import random

random_integer = random.randint(1, 100)
print(f'Random integer between 1 and 100: {random_integer}')

random_list = []
for i in range(6):
    random_list.append(random.randint(1, 100))

print(f'List of random numbers: {random_list}')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)

print(f'Shuffled list: {numbers}')'''
'''
import datetime

curr_datetime = datetime.datetime.now()
print(f'Current date and time: {curr_datetime}')

date1 = datetime.date(2026, 4, 24)
date2 = datetime.date(2026, 5, 22)
days_difference = (date2 - date1).days
print(f'Number of days between {date1} and {date2} is: {days_difference}')

formatted_date = curr_datetime.strftime("%d-%m-%Y")
print(f'Current date in DD-MM-YYYY format: {formatted_date}')'''


import os

curr_directory = os.getcwd()
print(f'Current working directory: {curr_directory}')

new_directory = 'test_directory'

if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f'Directory {new_directory} created.')
else:
    print(f'Directory {new_directory} already exists.')

if os.path.exists(new_directory):
    print(f'Verified: {new_directory} exists.')
else:
    print(f'{new_directory} does not exist.')

files_and_dirs = os.listdir(curr_directory)
print(f'Files and directories in the current directory:')
for item in files_and_dirs:
    print("-", item)
