# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
from easy5 import mk_dir, rm_dir, list_dir

def change_dir(folder):
    try:
        os.chdir(folder)
        print("Вы успешно перешли в директорию")
    except FileNotFoundError:
        print("Данной директории не существует")


do = {
    1: change_dir,
    2: list_dir,
    3: rm_dir,
    4: mk_dir
}

while True:
    choice = input("Выберите один из пунктов меню:\n"
                   "------------------------------\n"
                   "1. Перейти в директорию\n"
                   "2. Просмотреть содержимое текущей директории\n"
                   "3. Удалить директорию\n"
                   "4. Создать директорию\n"
                   "5. Выход\n\n")

    try:
        if len(choice.split()) == 2:  
            choice, folder_name = choice.split()
            choice = int(choice)
            if do.get(choice):
                do[choice](folder_name)
        else: 
            choice = int(choice)
            if choice == 5:
                break
            elif do.get(choice):
                print(do[choice]())
    except ValueError:
        print("Введены неверные данные!\n")
    except TypeError:
        print("Не указано имя директории!\n")
    
