# # генерация чистого списка 0.1
# start = int(input('Ведите число, с которого будет начинаться список = '))
# end = int(input('Введите число, каким будет заканчиваться список = ')) + 1
# step = int(input('Введите число (либо 1), это будет интервалом для списка между числами = '))
# list1 = [i for i in range(start, end, step)]
# print('Ваш массив сгенерирован:', list1, sep='\n')
# print('0.2')
# # генерация списка 0.2 минус: это все строки
# user_mass = int(input("Введите сколько элементов будет в списке: "))
# user_list = []
# i = 0
# while i < user_mass:
#     string = "Введите элемент #" + str(i + 1)+": "
#     user_list.append(input(string))
#     i += 1
# print('Ваш массив сгенерирован:', user_list, sep='\n')
#
# print(5 / 3)
# hello = 'vvvv'
# print(hello)
# del hello
# # print(hello)
# pers = True
# name = False
# print(type(pers))
# user_tf = bool(input('True or False: '))
# if user_tf and True == True:
#     print('Ваше выражение истина')
#     if not user_tf:
#         print('no no no')
#     else:
#         print('мне не чего сказать')
# user = int
# # user_name = user(input('Что вы хотели ввести?'))
# # print(user_name, type(user_name))
# user_text = input('Введите предложение: ')
# user_find = input('Введите то что хотите найти: ')
# number = 0
# for i in user_text:
#     if i == user_find:
#         number += 1
#         break
#     else:
#         number = 0
# print(number)
# list1 = [4, [1, 2, 3, 4, 5], 3, [2], 2, [3], 1, [4]]
# print(list1[1][2]) #[-1] последний(с конца) элемент
# # срезы, (функции строк -- отдельно)
# text = 'привет, сегодня погода хорошая не очень'
# print(text[0:7])
# print(text[0:-1:3])
# print(text[::-1])
# user_text = input('Введите предложение: ')
# print('Ваш текст наоборот: ', user_text[::-1], sep='\n')
# # [с чего: до куда: шаг]
# # кортежи(их нельзя изменить, но и памяти они занимают меньше (для оптимизации кода(как я пон)))
# test = (1, 2, 'True', True, 'мя мя мя')
# test1 = 1, 'hello', False, 7839, 'Сегодня хорошая погода'
# print(test1, test1.count('ля ля ля'), sep='\n')
# print(test.count(2), len(test))
# tuple1 = (7,) # это считается кортеж
# tuple2 = 7,
# tuple3 = (7) # а это уже нет
# user_text = input('Введите список: ')
# list1 = [user_text]
# tuple1 = tuple(list1)
# print('Теперь это кортеж', tuple1)
# dict1 = {
#     9: 1,
#     True: 2,
#     (1, 2, 3, 4, 5): 'hello',
#     'key1': 'val1'
# }
# print(dict1[('key1')])
# for key in dict1:
#     print(key)
# dict2 = dict(name='nast', last_name='mi mi', age=17)
# print(dict2)
# print(dict2.items())
# print(dict2.get('name'))
# # функции для словаря
# person = {
#     'user_0': {
#         'first_name': 'Nan',
#         'last_name': 'Nan',
#         'age': 00,
#         'address': ['г.Шумерля', 'Ул.nan'],
#         'grades': {'math': 3, 'ru': 4}
#     },
#     'user_1': {
#         'name': 'Nan',
#         'xxx': (1, 2, 3)
#     }
# }
# print(person['user_0']['address'][1])
# data = set('Привет, сегодня хорошая погода')
# data1 = {5, 6, 7, 7, 8, 9, 424, 424, 2442, 4324}
# print(data1)
# data.add('hello')
# # функции для множеств
# print(data)
# def p(i):
#     print(i, 'ваше число', sep='\n')
#
# a = int(input('Ведите число'))
# p(a)
# def p(el):
#     print(el)
#
#
# # после функции должен быть пропуск 2 строки
# p('hi')
# data1 = {5, 6, 7, 7, 8, 9, 424, 424, 2442, 4324}
# p(data1)
# анонимные функции
# test = lambda x, y: print(x * y)
# test(54, 0)
# Работа с файлами (после работы с файлы его надо закрыть)
# file = open('name/text.txt', 'w')
# # w(перезаписывает информацию)-
# если этого файла нет, то он создается и каждый раз при запуске стирается и записывается новая информация
# file.write('Hi, I`m \n already here.')
# # видимо только английский
# file.close()
# file = open('name/text.txt', 'a')
# # a - добавляет информацию
# file.write('Hi, I`m \n already here.')
# file.close()
# user_text = input('Введите текст(на английском пожалуйста): ')
# file = open('name/text.txt', 'w')
# file.write(user_text)
# file.close()
# чтение файла
# file = open('name/text.txt', 'r')
# # print(file.read(10))
# for line in file:
#     print(line, end="")
# file.close()
#
# мини программа
# user_text = input('Введите свое имя (до 20 символов): ')
#
# file = open('name/text.txt', 'w')
# file.write(user_text)
# file.close()
#
# file = open('name/text.txt', 'r')
# print(file.read(20))
# file.close()
#
# check = input('Это ваше имя?')
# if check == 'Да':
#     print('Удачного дня!!')
# else:
#     print('Что-то пошло не так ;(')
#
# Обработчик исключений
# try:
#     x = int(input('Введите число '))
#     y = int(input('Введите число '))
#     print('Summ - ', x + y)
# except ValueError:
#     print('Введите ЧИСЛО!')
# до тех пор пока пользователь не введет число
# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число '))
#         y = int(input('Введите число '))
#         print('Summ - ', x + y)
#     except ValueError:
#         print('Введите ЧИСЛО!')
#     else:
#         print('else')
#     finally:
#         print('End')
# finally закрывает try??? всегда сработает
# else если блок except не выполнился, а только try
# если произойдет ошибка к примеру: что не существует такого файла, то файл не будет закрыт(оптимизация)
# file = open('text.txt', 'r')
# print(file.read())
# file.close()
# правильно будет написать так -> даже если будет найдена ошибка файл будет закрываться
# try:
#     with open('text.txt', 'r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('файл не найден')
# модули или библиотеки
# import time
# time.sleep(3)
# таймер на 3 секунды
# print('hello')
# import datetime as d
# import sys, os
# либо в одну строчку
# import datetime as d, sys, os, platform
# print(d.datetime.now())
# print(sys.path)
# print(os.name)
# print(platform.system())
# гугл про библиотеки
# <- полный импорт библиотеки//// не полный импорт библиотеки ->
# имя библиотеки| функция| псевдоним \ через запятую можно не сколько ля
# from math import sqrt as s
# print(s(25))
# как создать свою библиотеку или скачать, это в интернет
# ООП только начало
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print('Name: ', self.name, "Age: ", self.age, "Happy: ", self.isHappy)
#
#     def __init__(self, name = None, age = None, isHappy = None):
#         # self.name = name
#         # self.age = age
#         # self.isHappy = isHappy
#         self.set_data(name, age, isHappy)
#         self.get_data()
#
#
# cat1 = Cat('Basilar', 3, True)
# # cat1.set_data('Basilar', 3, True)
# cat2 = Cat("барсик", 6, True)
# cat3 = Cat(7,'мой кот анон', False)
# # cat2.name = 'Барсик'
# # cat2.age = 6
# # cat2.isHappy = True
# # print(cat1.age)
# # print(cat2.name)
# # print(cat2.get_data())
# наследование, инкапсуляция, полиморфизм
# class magazin:
#     got = None
#     city = None
#
#     def __init__(self, got, city):
#         self.got = got
#         self.city = city
#
#     def det_info(self):
#         print('Год', self.got, "город", self.city, )
#
#
# class Shop(magazin):
#     pupils = 0
#
#     def __init__(self, pupils, got, city):
#         super(Shop, self).__init__(got, city)
#         self.pupils = pupils
#
#
# shop = magazin(1999, 'shumerlai')
# shop1 = Shop(5, 99, 'no')
# shop1.det_info()

