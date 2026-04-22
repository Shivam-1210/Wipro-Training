"""
Date : 22-04-2026
Desc: learning various if statements formats
"""
# big 2

# num1 = int(input('enter first number: '))
# num2 = int(input('enter second number: '))
#
# if num1 == num2:
#     print('both are equal number')
# elif num1 > num2:
#     print(num1 , ' is big. ')
# else:
#     print(num2 , 'is big. ')

#big 3

'''num1 = int(input('enter first number '))
num2 = int(input('enter second number '))
num3 = int(input('enter third number '))

if num1 == num2 and num2 == num3:
    print('All values are equal')

elif num2 > num1 and num2 > num3:
    print(num2, 'num2 is biggest')

elif num3 > num2 and num3 > num1:
    print(num3, 'num3 is biggest')
elif num1 > num2 and num1 > num3:
    print(num1, 'num1 is biggest')

'''

# weekdays

ch = int(input('enter a number between 1 and 7'))

match ch:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Invalid Choice')

