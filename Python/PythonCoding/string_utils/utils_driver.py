
from string_utils.string_operations import reverse_string, to_uppercase, string_length
from string_utils.string_validations import is_palindrome, is_alpha

string1 = 'Racecar'

print(f'Original text: {string1}')
print(f'Reversed: {reverse_string(string1)}')
print(f'Uppercase: {to_uppercase(string1)}')
print(f'Length: {string_length(string1)}')


print(f'Is palindrome? {is_palindrome(string1)}')
print(f'Contains only letters? {is_alpha(string1)}')