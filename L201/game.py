import random

number = random.randint(0, 10)
attempts = 3

while attempts > 0:
    guess = int(input(f"Попыток осталось: {attempts}. Угадайте число от 0 до 10: "))
    
    if guess < number:
        print("Неверно! Загаданное число больше.")
    elif guess > number:
        print("Неверно! Загаданное число меньше.")
    else:
        print("Поздравляем! Вы угадали число!")
        break
    
    attempts -= 1

if attempts == 0:
    print(f"Вы проиграли. Загаданное число было: {number}")
