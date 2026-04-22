
# natural number display

'''num = int(input('enter a number '))
value = 1

while value <= num:
    print(value)
    value+=1
'''

num = input('enter a number')
cnt = len(num)
sum = 0
ni = int(num)
comp = ni

while ni > 0:
    rem = ni % 10
    sum = sum + rem **cnt
    ni= ni//10

if comp == sum:
    print('Armonstrong number')

else:
    print('non Armonstrong number')

