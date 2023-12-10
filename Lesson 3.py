
'''var1 = 5

def func():
    global var1
    var1 += 3
    var_1 = 10
    print(var1)

func()
print(var1)'''


import random

def game(user_choice):
    computer_choice = random.choice("KNB")
    print(f"Комп'ютер - {computer_choice}, Гравець - {user_choice}")
    user_choice = str.upper(user_choice)
    if user_choice == computer_choice:
        return "D"
    elif computer_choice == "K" and user_choice == "N" or \
         computer_choice == "N" and user_choice == "B" or \
         computer_choice == "B" and user_choice == "K":
        return "C"
    elif computer_choice == "K" and user_choice == "B" or \
         computer_choice == "N" and user_choice == "K" or \
         computer_choice == "B" and user_choice == "N":
        return "U"

def print_result(winner, result):
    if winner == "D":
        print("В цьому раунді нічья")
    elif winner == "U":
        print("В цьому раунді переміг гравець")
        result["user"] += 1
    elif winner == "C":
        print("В цьому раунді переміг комп'ютер")
        result["computer"] += 1
    print("Поточний рахунок")
    print(f'Комп\'ютер - {result["computer"]}, Гравець - {result["user"]}')

result = {"user": 0, "computer": 0}

for i in range(3):
    print()
    print(f"======= РАУНД №{i+1} =======")
    choice = input("Виберіть K, N, B - ")
    print_result(game(choice), result)