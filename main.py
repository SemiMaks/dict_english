import random

from leaters import leaters

scores = 0


def train():
    scores = 0
    num = 3
    ans = 0
    dict_k = leaters.keys()
    print(dict_k)

    dict_v = leaters.values()
    print(dict_v)
    print()

    print('Приветствую тебя в языковом тренажёре!')
    print('Требуется перевести ', num, ' слов(a).')
    print('Что ж, приступим. Удачи!)')
    print()

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
            break

        print('Всего ты отгадал ', scores, 'слов(а)!')
        print()


train()
print('Благодарю за участие! Пока!')
