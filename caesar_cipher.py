def caesar_cipher_en(txt, step):
    ciphered_txt = ''
    for el in txt:
        if el.isalpha():
            if el.islower():
                ciphered_txt += chr(ord("a") + (ord(el) - ord("a") + 26 + step) % 26)
            else:
                ciphered_txt += chr(ord("A") + (ord(el) - ord("A") + 26 + step) % 26)
        else:
            ciphered_txt += el
    return ciphered_txt

def caesar_cipher_ru(txt, step):
    ciphered_txt = ''
    for el in txt:
        if el.isalpha():
            if el.islower():
                ciphered_txt += chr(ord("а") + (ord(el) - ord("а") + 32 + step) % 32)
            else:
                ciphered_txt += chr(ord("А") + (ord(el) - ord("А") + 32 + step) % 32)
        else:
            ciphered_txt += el
    return ciphered_txt

def caesar_decipher_en(txt, step):
    deciphered_txt = ''
    for el in txt:
        if el.isalpha():
            if el.islower():
                deciphered_txt += chr(ord("a") + (ord(el) - ord("a") + 26 - step) % 26)
            else:
                deciphered_txt += chr(ord("A") + (ord(el) - ord("A") + 26 - step) % 26)
        else:
            deciphered_txt += el
    return deciphered_txt

def caesar_decipher_ru(txt, step):
    deciphered_txt = ''
    for el in txt:
        if el.isalpha():
            if el.islower():
                deciphered_txt += chr(ord("а") + (ord(el) - ord("а") + 32 - step) % 32)
            else:
                deciphered_txt += chr(ord("А") + (ord(el) - ord("А") + 32 - step) % 32)
        else:
            deciphered_txt += el
    return deciphered_txt

direction = input('Выберите направление шифрования:\n(ш = шифрование; д = дешифрование)\n')
language = input('Выберите язык шифрования:\n(ru = русский; en = английский)\n')
if language == 'ru':
    step = int(input('Введите шаг сдвига (целое число от 1 до 31):\n'))
else:
    step = int(input('Введите шаг сдвига (целое число от 1 до 25):\n'))

txt = input('Введите текст:\n')

if direction == 'д':
    if language == 'ru':
        print(caesar_decipher_ru(txt, step))
    else:
        print(caesar_decipher_en(txt, step))
elif direction == 'ш':
    if language == 'ru':
        print(caesar_cipher_ru(txt, step))
    else:
        print(caesar_cipher_en(txt, step))