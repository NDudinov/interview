some_list = [4, 3, 5, 25, 26, 19, 25]


def my_sort(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

# Какой будет вывод функции my_sort(some_list) ?
# 1. [3, 4, 5, 19, 25, 25, 26]
# 2. [3, 4, 5, 25, 19, 25, 26]
# 3. [4, 3, 5, 25, 26, 19, 25]
# 4. [3, 4, 5, 25, 19, 26, 25]
