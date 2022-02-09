# s1 = 'spam"s'
# s2 = "spam’s"
# s3 = r'C:\newt.txt’
# s4 = r'\n\n\\'[:-1]
# s5 = r'\n\n' + '\\'
# s6 = '\\n\\n'
#
# print(s1 + s2)
# print(s1 * 3)
# print(len(s1))
# print(s1[0]+s1[2]+s1[-2])

# s = 'spam\neggs'
# print(s[3:5])
# print(s[2:-2])
# print(s[:6])

import random
import time


from random import randint, randrange


# print("Вывод случайного целого числа ", randint(0, 9))
# print("Вывод случайного целого числа ", randrange(0, 11, 5))
# # =================================
# city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# print("Выбор случайного города из списка - ", random.choice(city_list))
#
# list = [20, 30, 40, 50 ,60, 70, 80, 90]
# sampling = random.choices(list, k=5)
# print(f"Выборка с методом choices {sampling}, {sampling[1]}")

# Пишем программу выбора одежды на работу

clothes_list = ['Рубашка', 'Футболка', 'Шляпа', 'Брюки', 'Носки', 'Шуба', 'Кепка', 'Тапки', 'Платок', 'Плавки']
print("Выбор случайной одежды из списка - ", random.sample(clothes_list, k=4))