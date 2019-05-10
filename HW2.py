# Срезы
#name  = 'Анастасия'

# print(name[-1])
# print(name[0:4]) #от включая, до - не включая
# print(name[0:-1:3])
#print(name[::2])# [от:до:шаг]


email = 'supchik90@mail.ru'
# index = email.find('@')
# print(index)
# print(email[:index])

# name = 'ПеТроВ иВаНОв'
# print(name.l ower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(len(name))
# print(name.lower().count('о'))
# print(name.split())
# print(email.split('@'))
# address, domain = email.split('@')
# print(address, domain)

# .rjust()  .ljust() ИЗУЧИТЬ САМОСТОЯТЕЛЬНО

# name = 'Ivan'
# age = 50
# money = 500.50
# print('Hello', name, '. Вам ', age, ' лет. У вас в кармене ', money, ' рублей')
# result = 'Hello %s вам %i лет, у вас в кармене %f рублей'%(name, age, money)
# result = 'Hello {}, вам {} лет, у вас в кармане {} рублей'.format(name, age,money)
# result = f'Hello {name}, вам {age}, у вас в кармане {money} рублей'
# print(result)

# СПИСКИ
# name = 'Sergey'
# human = ['Ivan', 'Alex', 'Olga', name]
# print(human[1])
# print(human[1::2])
# human[0] = 'Nastya'
# human.append('Andrey')
# human.insert(1, 200)
# print(human.index('Alex'))
# human.remove('Olga')
# cutted_el = human.pop()
# print (human, 'Удален последний элемен ', cutted_el)
# print(human)
# print('Olga' in human)
# print('Vova' in human)
# x = [1,2,3, ['qwe', 213]]
# print(x[3][1])

# КОРТЕЖ
# human = (1,2,3,4,5,6)
# x = 0
# while x < len(human):
#     print(human[x])
#     x +=1

# for i in human:
#     print(i)
#
# for i in [1,2,3,4,5]:
#     print('Привет!')
# for i in range(5, 10):
#     print (i, 'Привет!')


# СЛОВАРЬ
# human = {
#     'name': 'Ivan',
#     'age': 25,
#     'money': 52.2
# }
# print(human['name'])
# human['data'] = [1, 2, 3, 4]
# print(human)
# # print(human['data'])
# print(human.get('qwe')) # прверка, есть ли такой элемент в словаре
# print(human.get('age'))
# human.pop('age')
# human.popitem()
# print(human)
# if human.get('data'):
#     print('data' присутствует)
# for key in human.keys():
#     print(key)
# for value in human.values():
#     print(value)
# for key, value in human.items():
#     print(key, value)
# for answer in human.items():
#     print(answer)

# МНОЖЕСТВА
# my_set = {1,1,1,1,1,1,2,2,23,5,43}
# print(my_set)
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a|b) объединение
# print(a == b)
# print(a & b)
# print(a - b)
# print(a ^ b) всё кроме пересечения


EASY
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# # Подсказка: воспользоваться методом .format()
# fruit = ['яблоко', 'банан', 'киви', 'арбуз']
# a = 1
# for i in fruit:
#     print (str(a) + '.' +'{0}'.format(i).rjust(10))
#     a += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
# things = ['одеяло', 'подушка', 'простыня', 'наволочка']
# clothes = ['наволочка', 'Рубашка', 'брюки', 'туфли']
# for i in things:
#     for w in clothes:
#         if i == w:
#             things.remove(i)
# print(things)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# a = [5, 8, 4, 3, 9, 1]
# b = []
# for i in a:
#     if (i % 2) == 0:
#         b.append(int(i / 4))
#     else:
#         b.append(int(i * 2))
# print(a)
# print(b)


# Task 2 NORMAL
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]