# for i in range(100):
#     new_str=str(i+1)
#     new_list = list(new_str)
#     if int(new_list[-1]) == 1 and i+1 != 11:
#         print('{} Процент'.format(i + 1))
#     elif int(new_list[-1]) > 1 and int(new_list[-1]) <= 4:
#         if  i+1> 10 and i+1<= 14:
#             print('{} Процентов'.format(i + 1))
#         else:
#             print('{} Процента'.format(i + 1))
#     else:
#         print('{} Процентов'.format(i + 1))

# # 1 минута
# one_minute = 60
# # 1 час
# one_hour = 3600
# # 1 день
# one_day = 86400
# # 1 неделя
# one_week = 604800
# # 1 месяц (30.44 дней)
# one_month = 2629743
# # 1 год (365.24 дней)
# one_year = 31556926
# duration = int (input('Укажите продолжительность в секундах: '))
# if duration<one_minute:
#     print ('{} сек'.format(duration))
# elif one_minute <= duration and one_hour > duration:
#     my_minute = duration // one_minute
#     my_second = duration % one_minute
#     print('{} мин {} сек'.format(my_minute, my_second));
# elif duration >= one_hour and duration < one_day:
#     my_hour=duration // one_hour
#     duration=duration % one_hour
#     my_minute = duration // one_minute
#     my_second = duration % one_minute
#     print ('{} час {} мин {} сек'.format(my_hour,my_minute,my_second));
# elif duration >= one_day and duration < one_week:
#     my_day = duration // one_day
#     duration=duration % one_day
#     my_hour = duration // one_hour
#     duration = duration % one_hour
#     my_minute = duration // one_minute
#     my_second = duration % one_minute
#     print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second));
# elif duration >= one_month and duration < one_year:
#     my_week = duration//one_week
#     duration=duration%one_week
#     my_day = duration // one_day
#     duration = duration % one_day
#     my_hour = duration // one_hour
#     duration = duration % one_hour
#     my_minute = duration // one_minute
#     my_second = duration % one_minute
#     print('{} нед {} дн {} час {} мин {} сек'.format(my_week, my_day, my_hour, my_minute, my_second));
# elif duration >= one_year:
#     my_year=duration//one_year
#     duration = duration % one_year
#     my_week = duration//one_week
#     duration=duration%one_week
#     my_day = duration // one_day
#     duration = duration % one_day
#     my_hour = duration // one_hour
#     duration = duration % one_hour
#     my_minute = duration // one_minute
#     my_second = duration % one_minute
#     print('{} год {} нед {} дн {} час {} мин {} сек'.format(my_year, my_week, my_day, my_hour, my_minute, my_second));


cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    '''
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    '''
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 1) : ',my_numbers_sum_list)

cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers =[]

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    '''
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    '''
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 2) : ',my_numbers_sum_list_even_numbers)


