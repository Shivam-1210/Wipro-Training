
numbers = input('Enter the numbers: ')

try:
    res = int(numbers)

except:
    print('non numeric string' )

else:
    print(f'the number is: {res}')