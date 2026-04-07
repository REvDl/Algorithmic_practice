"""Усложненная игра, тз составлено с помощью нейросети 'Gemini', к обычной игре добавлены пару изменений:
 выбор сложности, валидация, обратная связь, повторная игра
"""
import random
def check_guess(player_guess, computer_number, current_steps):
    """
    Проверяет предположение игрока и предоставляет обратную связь.

    Args:
        player_guess (int): Число, которое предположил игрок.
        computer_number (int): Число, загаданное компьютером.
        current_steps (int): Текущее количество шагов, сделанных игроком.

    Returns:
        bool: True, если игрок угадал число; False в противном случае.
    """
    if player_guess < computer_number:
        print("Загаданное число больше!")
        return False
    elif player_guess > computer_number:
        print("Загаданное число меньше!")
        return False
    else:
        print(f"\n🎉 Правильно! Загаданное число было: {computer_number}.")
        print(f"Ты справился за {current_steps} шагов! Молодец!")
        return True # Возвращаем True, так как число угадано


def get_validated_number(prompt, min_val, max_val):
    """
    Запрашивает у пользователя целое число в заданном диапазоне.

    Args:
        prompt (str): Сообщение, которое будет выводиться пользователю.
        min_val (int): Минимальное допустимое значение.
        max_val (int): Максимальное допустимое значение.

    Returns:
        int: Проверенное целое число, введенное пользователем.
    """
    while True: # Бесконечный цикл, пока не получим корректный ввод
        try:
            num_str = input(prompt)
            num = int(num_str)

            if min_val <= num <= max_val:
                return num
            else:
                print(f"Пожалуйста, введите число в диапазоне от {min_val} до {max_val}.")
        except ValueError:
            print("Вводить можно только целое число!")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
def play_game(min_num, max_num):
    num_computer = random.randint(min_num, max_num)
    steps = 0
    while True:
        steps += 1
        num_people = get_validated_number(f"ведите число от {min_num} до {max_num}: ", min_num, max_num)
        guess_is_correct = check_guess(num_people, num_computer, steps)
        if guess_is_correct:
            break

def get_menu_choice(menu_text, min_val, max_val):
    while True:
        print(f"\n{menu_text}") # Меню выводится здесь
        try:
            num_str = input("Введите ваш выбор: ") # Или prompt, как раньше
            num = int(num_str)

            if min_val <= num <= max_val:
                return num
            else:
                print(f"Ошибка: Введите число от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: Введены неверные данные, пожалуйста, введите число.")


menu = ("Добро пожаловать в игру с компьютером'Угадай число', сделайте свой выбор:\n"
        "1 - Легкий уровень сложности(от 1 до 50)\n"
        "2 - Средний уровень сложности (от 51 до 150)\n"
        "3 - Сложный уровень сложности (от 151 до 300)\n"
        "4 - выйти")
num_people = 0
while True:
    choices = get_menu_choice(menu, 1, 4)
    if choices == 4:
        print("Спасибо за игру! До свидания.")
        break
    if choices == 1:
        play_game(1, 50)
    elif choices == 2:
        play_game(51, 150)
    elif choices == 3:
        play_game(151, 300)

    play_again_choice = get_validated_number("Хотите сыграть ещё раз? (1 - Да, 2 - Нет)", 1, 2)
    if play_again_choice == 2:
        print("Спасибо за игру! До свидания")
        break