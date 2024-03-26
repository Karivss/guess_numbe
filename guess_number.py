from random import randint
num = randint(1,100)
print('Угадайте число от 1 до 100 ')
while True:
    guess = int(input())

    if guess < num:
        print('Ваше число меньше того, что загадано')
    
    if guess > num:
        print('Ваше число больше того, что загадано')

    if guess == num:
        break
print('Отличная интуиция! Вы угадали число :)')
