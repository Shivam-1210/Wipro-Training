
# Program to check the eligibility to vote

'''age = int(input('Enter the age: '))

if age >= 18:
    print('eligible to vote')
else:
    print('not eligible to vote')'''


# program to check leap year

'''year = int(input('Enter a year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Leap Year')
else:
    print('Not a leap year')'''


# divisibility by 5

'''num = int(input('Enter a number: '))

if num % 5 == 0:
    print(num, 'is divisible by 5')
else:
    print(num, 'is not divisible by 5')'''


# Program to check vowel or consonant

'''char1 = input('Enter a character: ').lower()

if len(char1) == 1 and char1.isalpha():
    if char1 in 'aeiou':
        print('The character is vowel')
    else:
        print('The character is consonant')

else:
    print('Invalid character')'''


'''# Ask the user to enter a password
password = input("Enter your password: ")

# Check if the password is at least 8 characters long
if len(password) >= 8:
    print("Your password is strong.")
else:
    print("Your password is weak. It should be at least 8 characters long.")'''

# Get grade input from the user
'''grade = input("Enter your grade (A, B, C, D, F): ").upper()  # Convert to uppercase to handle lowercase input

# Use match-case to print a message based on the grade
match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Very Good!")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:  # Default case if input doesn't match any of the above
        print("Invalid grade entered")
'''

# Get traffic light color input from the user
color = input("Enter traffic light color: ").capitalize()  # Capitalize to standardize input


match color:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid color entered")



# Program to print factorial of a number

'''num = int(input("Enter a number: "))

# Initialize the factorial result
factorial = 1

# Use a for loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Print the result
print('The factorial of',num , 'is', factorial)'''

# Program to print all even numbers between 1 and 20
'''
for num in range(2, 20, 2):
    print(num, end = '\t')'''

# program that uses a while loop to create a countdown timer from 10 to 0

'''count = 10
while count >= 0:
    print(count)
    count-=1'''

# Program that uses a for loop to count the number of vowels in a given string

'''str1 = input('Enter a string: ').lower()
cnt = 0
for ch in str1:
    if ch in 'aeiou':
        cnt+=1
print(cnt)'''

# Program to print numbers from 1 to 10, but skips printing the number 5 (use continue)
# and stops the loop if the number 8 is reached (use break).

for i in range(1, 11):
    if i == 5:
        continue
    elif i == 8:
        break
    print(i, end='\t')






