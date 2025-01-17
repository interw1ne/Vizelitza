import random


def load(file_path):
    with open(file_path, 'r', encoding='windows-1251') as file:
        words = [line.strip() for line in file if line.strip()]
    return words


def filtr_slow_dlin(words, length):
    return [word for word in words if len(word) == length]


def viz(words, attempts, word_length):
    print("Добро пожаловать в игру Виселица!")

    # Фильтруем слова по заданной длине
    filtered_words = filtr_slow_dlin(words, word_length)

    if not filtered_words:
        print(f"Нет слов длиной {word_length}. Попробуйте другую длину.")
        return

    # Выбираем случайное слово из отфильтрованного списка
    word = random.choice(filtered_words)
    word_dlin = len(word)

    true_letters = []
    pop = attempts
    word_disp = ['_'] * word_dlin

    while pop > 0 and '_' in word_disp:
        print("\nТекущие буквы: ", ' '.join(word_disp))
        print(f"Осталось попыток: {pop}")
        da = input("Введите букву: ").lower()

        if da in true_letters:
            print("Вы уже угадывали эту букву. Попробуйте другую.")
            continue

        true_letters.append(da)

        if da in word:
            print("Правильно!")
            for index, letter in enumerate(word):
                if letter == da:
                    word_disp[index] = da
        else:
            pop -= 1
            print("Неправильно!")

    if '_' not in word_disp:
        print(f"Поздравляем! Вы угадали слово: {word}")
    else:
        print(f"Вы проиграли! Загаданное слово было: {word}")


if __name__ == "__main__":
    words = load('russian.txt')  # Укажите путь к вашему файлу

    # Запрашиваем длину слова и количество попыток у пользователя
    dlin = int(input("Введите длину слова: "))
    pop = int(input("Введите количество попыток: "))

    viz(words, pop, dlin)