#Do the following in sequence and record the results in a single program

'''Create a list with 5 different types of fruits. Print the list.
Add two more fruits to the list, then remove one fruit from it. Print the updated list.
Access the second and fourth fruits in the list. Print them.
Slice the list to get the first three fruits and print the result.
Find and print the length of your list.'''

'''list1 = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
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
print(f'length of list3: {len(list3)}')'''



'''tup1 = ('Varanasi', 'Prayagraj', 'Lucknow')
print(tup1)
tup2 = tup1[::2]
print(tup2)
tup3 = ('Bangalore', 'Mumbai')
tup1 = tup1+tup3
print(tup1)
#tup1[2] = ('Noida')  # tuple don't support item assignment
city1 , city2, city3, city4, city5 = tup1
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)'''

'''
set1 = {'White','Black', 'Green', 'Blue', 'Red'}
print(set1)
set1.add('Grey')
set1.pop()
print(set1)
set2 = {'Yellow', 'pink', 'Violet'}
print(f'union_set = {set1 | set2}')
print(f'intersection_set = {set1 & set2}')
print(f'difference_set = {set1 - set2}')
if 'Red' in set1:
    print('Red is present in the set1')

Fruits = {'Apple', 'Banana', 'Mango', ' Orange', 'Apple', 'Mango'}
print(Fruits)'''



dict1 = {'name': 'XYZ', 'age': '23', 'fav_hobby': 'Cricket'}
print(dict1)
print(dict1['name'])
dict1['fav_food'] =  'Biryani'
dict1['fav_hobby'] = 'Badminton'
print(dict1)
print(f'keys: {list(dict1.keys())}')
print(f'values: {list(dict1.values())}')
dict1.pop('age')
print(dict1)
