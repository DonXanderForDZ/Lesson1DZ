a = int(input("Введите время в секундах "))
b = a % 60
c = a // 60
d = c // 60
c = c % 60
print(f"Получается {d} часов, {c} минут, {b} секунд")