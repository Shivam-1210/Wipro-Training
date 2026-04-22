Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hEllo'
s1.casefold()
'hello'
s1.count()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1.count()
TypeError: count expected at least 1 argument, got 0
s1.count(l)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1.count(l)
NameError: name 'l' is not defined
s1.count('l')
2
s1.index('o')
4
s1.find('0')
-1
>>> s1.endswith('o')
True
>>> s1.endswith('u')
False
>>> False
False
>>> s1 = 'hell067'
>>> s1.isdigit()
False
>>> s1 = '79'
>>> s1.isdigit()
True
>>> s1.replace('L,'l')
...            
SyntaxError: unterminated string literal (detected at line 1)
>>> s1.replace('L','l')
...            
'79'
>>> s1[1]
...            
'9'
>>> s1 = 'hello dost'
...            
s1[5]
           
' '
s1[3]
           
'l'
s1[0:5]
           
'hello'
s1[0:7]
           
'hello d'
