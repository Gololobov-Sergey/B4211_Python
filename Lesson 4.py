

'''def func(*args, length):
    print(type(args))
    for arg in args:
        print(arg)

func(12, 345, "234", True, length=10)

a = 1,2,3

def func1(**kwargs):
    print(type(kwargs))
    #for key in kwargs.keys():
    #    print(key, kwargs[key])
    for key, value in kwargs.items():
        print(key, value)

func1(name="Nic", age=20, length=100)

def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func2(1,34,"23", name=23, age=20)'''


import random

players = []
list_action = ["Помий посуд", "Сходи за хлібом", "Зроби уроки"]
list_question = ["Як пройшов твій день", "Як тебе називають у школі", "Хто твій найкращій друг"]


def get_players(players):
    while True:
        name = input("Введіть ім'я гравця : ")
        players.append(name)
        if len(players) < 2:
            continue
        else:
            next = input("Чи хочете ще додати гравця? (Y/N) ")
            if str.upper(next) == "Y":
                continue
            else:
                break

def game(list_action, list_question, players):
    for name in players:
        choice = input(f"Вибір для {name}: Правда або Дія? P/D ")
        if str.upper(choice) == 'P':
            q_index = random.randint(0, len(list_question) - 1)
            print(list_question[q_index])
            list_question.pop(q_index)
        elif str.upper(choice) == 'D':
            a_index = random.randint(0, len(list_action) - 1)
            print(list_action[a_index])
            list_action.pop(a_index)

        if len(list_action) == 0 or len(list_question) == 0:
            return False
    return True



get_players(players)
while True:
    if not game(list_action, list_question, players):
        print("Нажаль закінчилися запитання. Гру закінчено...!")
        break
