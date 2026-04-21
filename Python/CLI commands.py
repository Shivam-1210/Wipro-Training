Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=5
b = float(5)
b
5.0
c='7'
d = int(c)
d
7
x='h'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'h'
x=i
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x=i
NameError: name 'i' is not defined. Did you mean: 'id'?
x='i'
y = ord(x)
y
105
x = ' '
y = bool(x)
y
True
print(5)
5
print('ans: ', 8+9)
ans:  17
print('ans:' + 9)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print('ans:' + 9)
TypeError: can only concatenate str (not "int") to str
print('my brother's house)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('my brother's house')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("my brother's house")
...       
my brother's house
>>> input()
...       
hi
'hi'
>>> p = input(type: )
...       
SyntaxError: invalid syntax
>>> p = input('type:' )
...       
type:7865
>>> p
...       
'7865'
>>> p = int(input('type:' ))
...       
type:768
>>> p
...       
768
>>> 
===================== RESTART: C:/Wipro Training/Python/firstpgm.py ====================
namste everyone
>>> 
======================= RESTART: C:/Wipro Training/Python/sum.py =======================
sum is:  14
>>> 
======================= RESTART: C:/Wipro Training/Python/sum.py =======================
enter a number7
enter another number9
sum is:  16
