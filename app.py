# -*- coding: utf-8 -*-
from math import sqrt
nextOperation = 'yes'
memory = {}
history = []
def setMemory(key, value):
    memory[key] = value
    print(f"{value} збережено в пам'ять за ключем '{key}'")

def getMemory(key):
    if key in memory:
        print(memory[key])
    else:
        print("Не знайдено нічого за заданим ключем")

def setHistory(expression, result):
    history.append(f"{expression} = {result}")

def getHistory():
    if history:
        print("Історія обчислень:")
        for i in history:
            print(i)
    else:
        print("Обчисліть щось, перш ніж використовувати історію")

roundNum = int(input("Скільки знаків після коми ми використовуємо [0-5]>>"))

while nextOperation == "yes":

    if roundNum >= 0 and roundNum <= 5:
        fist_num = input("Введіть перше число, або якщо хочете отримати значення з пам'яті, введіть 'memory', або якщо хочете переглянути історію введіть 'history'>>")
        
            
        if fist_num == 'memory':
            memoryKey = input("Введіть ключ для отримання його з пам'яті>>")
            fist_num = getMemory(memoryKey)
            if fist_num is None:
                continue
        elif fist_num == 'history':
            getHistory()
            continue
        else:
            fist_num = float(fist_num)

        operation = input("Введіть операцію>>")


        if operation == "sqrt":
            if fist_num >= 0:
                result = round(sqrt(fist_num), roundNum)
                setHistory(f"sqrt{fist_num}", result)
            else:
                print("Неможливо отримати квадратний корінь від від'ємного числа")
                continue
        else:
            second_num = float(input("Введіть друге число>>"))
            if operation == "+":
                result = round(fist_num + second_num, roundNum)
            elif operation == "-":
               result = round(fist_num - second_num, roundNum)
            elif operation == "*":
                result = round(fist_num * second_num, roundNum)
            elif operation == "/":
                if second_num != 0:
                    result = round(fist_num / second_num, roundNum)
                else:
                    print("Номожна ділити на 0")
                    continue
            elif operation == "^":
                result = round(fist_num ** second_num, roundNum)
            elif operation == "%":
                result = round(fist_num % second_num, roundNum)
            else: 
                print("Невідома дія")
                continue

            setHistory(f"{fist_num} {operation} {second_num}", result)
    else:
        print("Некоректне значення знаків після коми")
        continue
    print(result)
    saveResult = input("Зберегти результат? yes/no>>")
    if saveResult == 'yes':
        memory_key = input("Введіть ключ для його збереження у пам'ять>>")
        setMemory(memory_key, result)
    nextOperation = input("Введіть 'yes' щоб продовжити, або любу іншу клашіву, щоб завершити програму>>")