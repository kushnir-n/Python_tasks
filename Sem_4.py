#Задача 1
#Напишите функцию для транспонирования матрицы

print("Задача #1")

#создаем матрицу
a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

#функция транспонирования матрицы
def matrix_transpose(a):
    return [*zip(*a)]

#вызываем функцию    
print(matrix_transpose(a))

#Задача 2
#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если
#ключ не хешируем, используйте его строковое представление.

print ("\nЗадача #2")

def return_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'Возвращаю словарь: ключ = "{value}", значение = {key}')

return_dict(понедельник=29, вторник=30, среда=31, четверг=1, пятница=2, суббота=3, воскресенье=4)

#Задача 3

print ("\nЗадача #3")
#Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

MIN_SUM = 50
COMMISSION = 0.015
BONUS = 0.03
TAX = 0.1

#coo = count of operations; loo = list of operations

def put_money(cash: int, balance: float, coo: int, loo: list):
    balance = check_richness(balance)
    if cash % MIN_SUM == 0:
        balance += cash
        save_operation("Пополнен счёт на " + str(cash), loo)
        balance = check_bonus(balance, coo, loo)
        print("Текущий счёт: " + str(balance))
        return balance
    else:
        print("Сумма пополнения и снятия должны быть кратны 50")
        return balance

def withdraw_money(cash: int, balance: float, coo: int, loo: list):
    balance = check_richness(balance)
    if balance > 0:
        if balance - (cash + calculate_commission(cash)) >= 0:
            if cash % MIN_SUM == 0:
                balance -= cash + calculate_commission(cash)
                save_operation("Снятие со счёта: " + str(cash) + ", комиссия: " + str(calculate_commission(cash)), loo)
                balance = check_bonus(balance, coo, loo)
                print("Текущий счёт: " + str(balance))
                return balance
            else:
                print("Сумма пополнения и снятия должны быть кратны 50")
                return balance
        else:
            print("На вашем счету нет такой суммы денег")        
            return balance
    else:
        print("На вашем счету нет денег")
        return balance

def exit_atm():
    print("Работа банкомата завершена")
    exit()

def save_operation(action: str, loo: list):
    loo.append(action)

def calculate_commission(cash: int):
    if cash * COMMISSION < 30:
        return 30
    elif cash * COMMISSION > 600:
        return 600
    else:
        return cash * COMMISSION
    
def check_richness(balance: float):
    if balance > 5000000:
        print("На вашем счету более 5 млн. у.е.\nВычтен налог на богатство в размере " + str(balance * TAX))
        return balance - balance * TAX
    else:
        return balance        

def play_bankomat():
    balance = 0
    count_of_operations = 0
    list_operations = []
    game = True
    while (game):
        show_menu()
        input_str = input()
        if input_str == str(1):
            print("Пополнение счёта. Введите сумму:")
            count_of_operations = inc_coo(count_of_operations)
            balance = put_money(int(input()), balance, count_of_operations, list_operations)
        elif input_str == str(2):
            print("Снятие со счёта. Введите сумму:")
            count_of_operations = inc_coo(count_of_operations)
            balance = withdraw_money(int(input()), balance, count_of_operations, list_operations)            
        elif input_str == str(3):
            print("История операций:")
            print(list_operations)
        elif input_str == str(4):
            print("Баланс: " + str(balance))
        elif input_str == str(0):
            game = False
        else:
            print("Некорректный ввод. Попробуйте снова")
    exit_atm()

def inc_coo(coo: int):
    return coo + 1

def check_bonus(balance: float, coo: int, loo: list):
    if (coo > 0 and coo % 3 == 0):
        save_operation("Вам начислен бонус в размере " + str(balance * BONUS) + " у.е.", loo)
        print("Зачислен бонус за каждую 3-ю операцию")
        return balance + balance * BONUS
    else:
        return balance

def show_menu():
    print("===Банкомат===\n1 - пополнить счёт;\n2 - снять бабос;\n3 - показать историю операций\n4 - показать баланс\n0 - выход")

play_bankomat()