import random
import string


def generate_password(length=20):
    if length < 1:
        raise ValueError("Длина пароля должна быть не меньше 1")

    symbols = list(string.punctuation)
    numbers = list('0123456789')
    letters = list(string.ascii_letters)
    final_line = ""

    all_symbols = [symbols, numbers, letters] * 2 + [letters]  # Повышаем шанс выпадения букв

    for _ in range(length):
        choice = random.choice(all_symbols)

        # Проверка, чтобы не выбирать из пустого списка
        if not choice:
            continue

        char = random.choice(choice)
        final_line += char
        choice.remove(char)  # Удаляем символ, чтобы избежать повторов

    return final_line


if __name__ == "__main__":
    try:
        user_length = int(input("Введите желаемую длину пароля: "))
        password = generate_password(user_length)
        print("Сгенерированный пароль:", password)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
