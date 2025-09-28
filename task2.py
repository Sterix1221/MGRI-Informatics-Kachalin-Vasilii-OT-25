import random

def make_guess(min_value, max_value):
    return (min_value + max_value) // 2

def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    secret_number = random.randint(1, 100)
    human_attempts = 0
    min_value = 1
    max_value = 100


    bot1_name = 'Биба'
    bot1_attempts = 0
    bot2_name = 'Боба'
    bot2_attempts = 0

    while True:
        user_guess = input('Введите число от 1 до 100: ')

        if not user_guess.isdigit():
            print('Введите корректное число')
            continue

        user_guess = int(user_guess)
        human_attempts += 1

        if user_guess < secret_number:
            print('Загаданное число больше')
            min_value = max(min_value, user_guess + 1)
        elif user_guess > secret_number:
            print('Загаданное число меньше')
            max_value = min(max_value, user_guess + 1)
        else:
            print(f'Поздравляем вы угадали число {secret_number} с {human_attempts} попытки')
            break

        bot1_guess = make_guess(min_value, max_value)
        bot1_attempts += 1

        print(f'{bot1_name} выбрал: {bot1_guess}')
        if bot1_guess < secret_number:
            print('Загаданное число больше')
            min_value = max(min_value, bot1_guess + 1)
        elif bot1_guess > secret_number:
            print('Загаданное число меньше')
            max_value = min(max_value, bot1_guess + 1)
        else:
            print(f'{bot1_name} угадал число {secret_number} с {bot1_attempts} попытки')
            break
        
        bot2_guess = make_guess(min_value, max_value)
        bot2_attempts += 1
        
        print(f'{bot2_name} выбрал: {bot2_guess}')
        if bot2_guess < secret_number:
            print('Загаданное число больше')
            min_value = max(min_value, bot2_guess + 1)
        elif bot2_guess > secret_number:
            print('Загаданное число меньше')
            max_value = min(max_value, bot2_guess + 1)
        else:
            print(f'{bot2_name} угадал число {secret_number} с {bot2_attempts} попытки')
            break


guess_number()