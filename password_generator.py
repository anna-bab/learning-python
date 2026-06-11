import random

# строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

how_many_passwords = int(input('Сколько паролей необходимо сгенерировать?\n'))
password_length = int(input('Введите длину одного пароля\n(не менее 4-х символов):\n'))
include_numbers = input('Пароль должен включать в себя цифры?\n(д = да, н = нет)\n').lower()
if include_numbers in ('l', 'д'):
    chars += digits
include_lowercase_letters = input('Пароль должен включать в себя прописные буквы?\n(д = да, н = нет)\n').lower()
if include_lowercase_letters in ('l', 'д'):
    chars += lowercase_letters
include_uppercase_letters = input('Пароль должен включать в себя строчные буквы?\n(д = да, н = нет)\n').lower()
if include_uppercase_letters in ('l', 'д'):
    chars += uppercase_letters
include_punctuation = input('Пароль должен включать в себя символы "!#$%&*+-=?@^_"?\n(д = да, н = нет)\n').lower()
if include_punctuation in ('l', 'д'):
    chars += punctuation
exclude_questionable = input('Исключать ли неоднозначные символы "il1Lo0O"?\n(д = да, н = нет)\n').lower()


if exclude_questionable in ('l', 'д'):
    for char in "il1Lo0O":
        chars = chars.replace(char, '')
        digits = digits.replace(char, '')
        lowercase_letters = lowercase_letters.replace(char, '')
        uppercase_letters = uppercase_letters.replace(char, '')

def generate_password(chars, length):
    password = ''
    if include_numbers in ('l', 'д'):
        password += random.choice(digits)
    if include_lowercase_letters in ('l', 'д'):
        password += random.choice(lowercase_letters)
    if include_uppercase_letters in ('l', 'д'):
        password += random.choice(uppercase_letters)
    if include_punctuation in ('l', 'д'):
        password += random.choice(punctuation)
    for _ in range(length - len(password)):
        password += random.choice(chars)
    password = list(password)
    random.shuffle(password)
    return ''.join(password)

for _ in range(how_many_passwords):
    print(generate_password(chars, password_length))