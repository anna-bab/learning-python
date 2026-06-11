import random

print('Добро пожаловать в числовую угадайку')
print('Укажите правую границу диапазона, число > 1:')
right_limit = int(input())
def is_valid(s, limit):
    if 1 <= int(s) <= limit:
        return True
    else:
        return False 
    
def start_game(limit): 
    my_num = random.randint(1, limit)
    #print('my_num =', my_num)   
    n = 0
    while True:
        print('Ведите число от 1 до ', limit, ':', sep='') 
        num = input()
        n += 1
        if not is_valid(num, limit):
            print('А может быть все-таки введем целое число от 1 до ', limit, '?', sep='')
        else:
            num = int(num)
            if num < my_num:
                print ('Ваше число меньше загаданного, попробуйте еще разок')
            elif num > my_num:
                print('Ваше число больше загаданного, попробуйте еще разок') 
            else:
                print('Вы угадали, поздравляем!')   
                break

    print('Количество попыток:', n)
    print('Хотите сыграть еше раз? Наберите Y, если Да, или что-нибудь другое, если нет.') 

start_game(right_limit)    

while True:
    if input() == 'Y':
        print('Укажите правую границу диапазона, число > 1:')
        right_limit = int(input())
        start_game(right_limit)
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break