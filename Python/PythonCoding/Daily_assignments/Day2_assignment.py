#Do the following in sequence and record the results in a single program

'''Create a list with 5 different types of fruits. Print the list.
Add two more fruits to the list, then remove one fruit from it. Print the updated list.
Access the second and fourth fruits in the list. Print them.
Slice the list to get the first three fruits and print the result.
Find and print the length of your list.'''

list1 = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
print(list1)
list1.extend(['Blackberry' ,'pomogranate'])
list1.pop()
print(list1)
list2 = list1[1:4:2]
print(list2)
list3 = list1[:3]
print(list3)
print(f'length of list1: {len(list1)}')
print(f'length of list2: {len(list2)}')
print(f'length of list3: {len(list3)}')

