
list1 = list(map(int,input('Enter the list of numbers separated by spaces: ').split()))
index = int(input('enter an index value:'))

try:
    list2 = list1[index]
    print(list2)
except IndexError:
    print('Invalid Index')


