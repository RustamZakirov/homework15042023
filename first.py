# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8



list = []
a = int(input("Введите число: "))
list.append(0)
list.append(1)
n = int (2)
while (n < a + 1):
    list.append(list[n - 1] + list[n - 2])
    n += 1
print(f"{a} -> {list}")
