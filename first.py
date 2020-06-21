data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35, 35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22, 9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47, 4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]


# 1.1


def unique_data(element):
    new_array = []
    for i in element:
        if element.count(i) == 1:
            new_array.append(i)
    return new_array


print('Список уникальных чисел: ')
print(unique_data(data))


# 1.2


def non_meeting(element):
    check_number = 0
    new_array = []
    for i in element:
        while check_number <= 40:
            if element.count(check_number) == 0:
                new_array.append(check_number)
            check_number += 1
    return new_array


print('Список чисел <=40, не встречающихся в списке: ')
print(non_meeting(data))


# 1.3


def format_number_count(element):
    dictionary = {}
    for i in element:
        dictionary[i] = element.count(i)
    list_items = list(dictionary.items())
    list_items.sort(key=lambda x: (x[1], x[0]), reverse=True)
    return list_items


print('Сортировка по убыванию в формате (num: num_count): ')
print(format_number_count(data))


# 1.4


def standard_deviation(element):
    import math
    summ = 0
    arith_mean = sum(element)/len(element)
    for i in element:
        summ += (i-arith_mean) ** 2
    deviation = math.sqrt(summ/len(element))
    return deviation


print('СКО: ')
print('%.3f' % standard_deviation(data))