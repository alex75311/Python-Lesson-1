# # step1
# a = 10
# b = 'stroka'
# c = ('tupple1', 'tupple2', 'tupple3')
# d = [1, 2, 3, ]
# e = 8.123
# f = True
# g = {"name": "name1", "surname": "surname1"}
# print(f'integer {a}, string {b}, tupple {c}, list {d}, float {e}, boolean {f}, dictionary {g}')
#
# int1 = int(input('Введите первое число '))
# int2 = int(input('Введите второе число '))
# str1 = input('Введите первую строку ')
# str2 = input('Введите вторую строку ')
# print(f''' Первое число {int1} \n Второе число {int2} \n Первая строка {str1} \n Вторая строка {str2} ''')
#
# # step2
# time_sec = int(input('Введите время в секундах '))
# hour, minutes, sec = 0, 0, 0
# if time_sec >= 60:
#     minutes = time_sec // 60
#     sec = time_sec % 60
#     if minutes >= 60:
#         hour = minutes // 60
#         minutes = minutes % 60
# if sec < 10:
#     sec = '0' + str(sec)
# if minutes < 10:
#     minutes = '0' + str(minutes)
# if hour < 10:
#     hour = '0' + str(hour)
# print(f'{hour}:{minutes}:{sec}')
#
# # step3
# n = int(input('Вариант 1. Введите число '))
# result = n + (n*11) + (n*111)
# print(result)
#
# n = int(input('Вариант 2. Введите число '))
# result = n + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))
# print(result)

# step4
n = int(input('Введите целое положительное число '))
max_num = 0
while n % 10 > 0:
    x = n % 10
    if max_num < x:
        max_num = x
    n = n // 10
print(max_num)