import math


def min_boxes(items):
    return math.ceil(items / 5)


num_items = int(input("Введите количество предметов: "))
print(f"Минимальное количество коробок: {min_boxes(num_items)}")
