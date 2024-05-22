# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

# import random


# Здесь пишем код
import random
import string

def generate_random_name():
    while True:
        # Генерируем две случайные длины для слов
        len1 = random.randint(1, 15)
        len2 = random.randint(1, 15)

        # Генерируем два случайных слова используя эти длины
        word1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(len1))
        word2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(len2))

        # Соединяем слова через пробел и выводим результат
        yield f'{word1} {word2}'

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))