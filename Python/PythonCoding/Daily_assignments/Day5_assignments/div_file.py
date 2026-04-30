
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))


try:
    res = num1 / num2

except ZeroDivisionError:
    if num2 == 0:
        print('num2 cannot be zero ')
except ValueError:
    if num1 ==str(num1) or num2 ==str(num2):
        print('Invalid numbers ')

else:
    print(f'Result of division: {res}')


