def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"


num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")
