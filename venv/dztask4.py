a = []
a = input("Введите целое положительно число ")
i = 0
b = a[0]
b = int(b)
while i < len(a):
    c = a[i]
    c = int(c)
    i += 1
    if b < c:
        b = c
    else:
        continue

print(f"Наибольшая цифра в числе {b}")