import random

from leaters import leaters

score = 0


def train():
    dict_k = leaters.keys()
    print(dict_k)

    dict_v = leaters.values()
    print(dict_v)

    while True:
        res, let = key, val = random.choice(list(leaters.items()))
        print('Напиши перевод слова: ', str(res))
        answer = input()
        if answer == let:
            print('Всё верно, это будет - ', str(let))
            # print()
            # score = +1
            # print(score)
        else:
            print('Не правильно!')
            break


train()
print('Ты отгадал слов:', score)
print('Благодарю за участие! Пока!')
