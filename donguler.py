print("1'den 100'e kadar olan sayılar:")
for sayi in range(1, 101):
    print(sayi)


print("1'den 100'e kadar olan çift sayılar:")
for sayi in range(1, 101):
    if sayi % 2 == 0:
        print(sayi)


sayi = int(input("Bir sayı giriniz (faktöriyel hesaplamak için): "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")


print("1'den 100'e kadar olan asal sayılar:")
for sayi in range(2, 101):
    asal = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi)
