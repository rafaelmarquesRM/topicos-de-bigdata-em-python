N = 12
contador = 0

for i in range(N):
    if i % 2 == 0:
        print("par")
        contador += 1
    if i % 5 == 0:
        print("cinco")
        contador += 1
    if contador > 10:
        print("cansei")