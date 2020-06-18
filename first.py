data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35, 35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22, 9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47, 4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]

# 1.1


def unique_data(element):
    new_array = []
    for i in element:
        if element.count(i) == 1:
            new_array.append(i)
    return new_array


print(unique_data(data))


# 1.2


def non_meeting(element):
    max_number = max(element)
    check_number = 0
    new_array = []
    for i in element:
        while check_number < max_number:
            if element.count(check_number) == 0:
                new_array.append(check_number)
            check_number += 1
    return new_array


print(non_meeting(data))