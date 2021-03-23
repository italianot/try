#1-2
# name = input("Как вас зовут? ")
# print("Приветствую " + name + "!")
#
# x = input("Введите число и я выведу его квадрат ")
# x = int(x)
# doublex = pow(x, 2)
# print("Квадрат", x, "равен", doublex)
#
# x = input("Введите длину ребра куба и я выведу объем куба, площадь его боковой поверхности и площадь грани ")
# x = int(x)
# v = pow(x, 3)
# s = 4*pow(x,2)
# sgr = pow(x, 2)
# print("Объем куба равен", v,
#       "Площадь боковой поверхности равна",s,
#       "Площадь грани куба", sgr)


#3
# x = int(input())
# if x>0:
#     print("число положительное")
# elif x<0:
#     print("число отрицательное")
# else:
#     print("число ноль")


#4
# a = int(input())
# b = int(input())
# if a==b:
#     print("числа равны")
# elif a>b:
#     print(a,"больше чем",b)
# elif a<b:
#     print(a, "меньше чем", b)


#5
# a = int(input("Введите число от 1 до 7 "))
# if a == 1:
#     print('Понедельник')
# elif a == 2:
#     print('Вторник')
# elif a == 3:
#     print('Среда')
# elif a == 4:
#     print('Четверг')
# elif a == 5:
#     print('Пятница')
# elif a == 6:
#     print('Суббота')
# elif a == 7:
#     print('Воскресенье')
# else:
#     print('Вы ввели неверное число')


#6
# days = {
#     1: 'Понедельник',
#     2: 'Вторник',
#     3: 'Среда',
#     4: 'Четверг',
#     5: 'Пятница',
#     6: 'Суббота',
#     7: 'Воскресенье'
# }
# a = int(input("Введите число от 1 до 7 "))
# #day = days.get(a)
# #print(day)
# print(days.get(a))


#7
# a = (input("Введите число от 1 до 99 "))
# ost = int(a) % 2
# length = len(a)
# if ost == 0:
#     if length == 1:
#         print("однозначное четное")
#     elif length == 2:
#         print("двухзначное четное")
# elif ost == 1:
#     if length == 1:
#         print("однозначное нечетное")
#     elif length == 2:
#         print("двухзначное нечетное")


#8
# seasons = {
#     "Зима": 'декабрь январь, февраль',
#     "Весна": 'март, апрель, май',
#     "Осень": 'сентябрь, октябрь, ноябрь',
#     "Лето": 'июнь, июль, август',
#     "зима": 'декабрь январь, февраль',
#     "весна": 'март, апрель, май',
#     "осень": 'сентябрь, октябрь, ноябрь',
#     "лето": 'июнь, июль, август'
# }
# a = input("Введите время года ")
# print(seasons.get(a))


#9
# seasons = {
#     "январь": 'JANUARY',
#     "февраль": 'Josh Groban - February Song',
#     "март": 'march',
#     "апрель": 'April ',
#     "май": 'Beliy, Xamm - Май',
#     "июнь": 'June ',
#     "июль": 'Noah Cyrus - July',
#     "август": 'Intelligency - August',
#     "сентябрь": 'Green Day - Wake Me Up When September Ends',
#     "октябрь": 'October - Evanescence',
#     "ноябрь": 'Guns N" Roses - November Rain',
#     "декабрь": 'abba happy new year'
# }
# a = input("Введите месяц ")
# print(seasons.get(a))


#10
# item = ["солнце", "что нибудь", "абракадабра",
#           "TV", "phone?"]
# a = int(input("Введите число ")) - 1
# c = len(item)
# if a > c or c <= 0:
#     print("пользователь редиска")
# else:
#     print(f"""
#     список имеет вид: {item}
#     {a+1} элемент в списке: {item[a]}
#     количество элементов: {len(item)}
#     """)

#11
# item = ["солнце", "что нибудь", "абракадабра",
#         "TV", "phone?"]
# a = input("Введите что нибудь ")
# if a in item:
#     i = item.index(a)
#     print(f"{a} находится на {i + 1} позиции в списке {item}")
# else:
#     print("Элемента нет в списке")


#12
# start_value = int(input())
# step = int(input())
# i = 0
#
# while i <= 4:  # пока i меньше четырех
#     print(f"i = {i} | {i+1} <= 4 == {i<=4} | значение = {start_value + i * step}")
#     i = i + 1  # и счетчик наращивай
#
# print("цикл завершен")
# print(f"Максимальное значение i = {i}")
#
# if i % 2 == 0:
#     print(f"i = {i} - четное")
# else:
#     print(f"i = {i} - нечетное")



#13
start = int(input())
fin = int(input())
while start <= fin:
    print(pow(start,2))
    start = start + 1


