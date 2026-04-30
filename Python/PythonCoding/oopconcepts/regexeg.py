

import re
'''
txt = input('Enter a text ') # India is my country
beg_pat = input('Enter beginning pattern ') # India
end_pat = input('Enter ending pattern ') #country
beg_pat = '^' + beg_pat  # ^India
end_pat = end_pat + '$' # try$

if re.search(pattern=beg_pat, string=txt):
    print('Beginning pattern available ')
else:
    print('Beginning pattern not available ')

if re.search(pattern=end_pat, string=txt):
    print('ending pattern available ')
else:
    print('ending pattern not available ')'''

#digit
'''mb_no = input('Enter a text ')
pat = r"\d"

if re.fullmatch(pattern=pat, string=mb_no):
    print('Only digits')

else:
    print('Other char available')'''

#username

'''un = input('Enter UN ')
pat = r"^[a-z_]{8,}$"

if re.match(pattern=pat, string=un):
    print('Valid')
else:
    print('Invalid')'''

#email

'''email_add = input('Email: ')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string=email_add):
    print('Valid')
else:
    print('Invalid')'''

#pwd
'''
pwd_txt = input('pwd: ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[-_@]).{8,}$"

if re.match(pattern=pat, string=pwd_txt):
    print('Valid')
else:
    print('Invalid')'''



txt = input('Enter text: ')
pat = r"\s+"

#print(re.sub(pattern=pat, string=txt, repl=' '))

print(re.split(pattern=pat, string=txt))

