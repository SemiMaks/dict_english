import random
from art import *

from leaters import leaters

scores = 0
hr = '-' * 20
status = '1'


#
# def works():
#     if status == 1:
#         train()
#     else:
#         print('Хорошего вам Дня!')


def train():
    try:
        status = 1
        while status >= 1:
            scores = 0
            ans = 0
            tprint("dict_english\n",font="white_bubble")
            print(hr + hr)
            print('Приветствую в языковом тренажёре!')
            print(hr + hr)
            print('Сколько слов готов перевести?:')
            num = int(input())

            # print('.....проверка подгружаемого словаря.....')
            # dict_k = leaters.keys()
            # print('Ключи:')
            # print(dict_k)
            #
            # dict_v = leaters.values()
            # print('Значения:')
            # print(dict_v)
            # print()

            print('Что ж, начинаем отгадывать ', num, ' слов(a).')
            print('Приступим. Удачи!)')
            # print(status)

            while ans != num:
                res, let = key, val = random.choice(list(leaters.items()))
                print('Переведи слово: ', str.capitalize(res))
                answer = input()
                answer = str.lower(answer)
                if answer == str.lower(let):
                    print('Всё верно, это - ', str.lower(let))
                    ans += 1
                    scores += 1
                else:
                    print('Не правильно!')
                    print(str.capitalize(key), ' это -', let)
                    print('Верно отгадано слов: ', scores)
                    print('Попытаться ещё раз нажми - 1, для завершения работы программы - 0')
                    status = int(input())
                    continue

            print('Всего ты отгадал ', scores, 'слов(а) из', num, 'слов!')
            print()
            print('Чтобы повторить нажмите - 1, для завершения работы программы - 0')
            status = int(input())
        # print(status)
        return status

    except Exception as er:
        print('Ошибка при выполнении программы!!!', er)
    finally:
        print('Работа программы успешно завершена!')


train()

print('Благодарю за участие! Пока!')
print(hr)
input("Для выхода нажми любую клавишу...")
