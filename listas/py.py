a = [float(input("Informe um valor: ")) for _ in range(5)]
b = [float(input("Informe um valor: ")) for _ in range(5)]
c = [num for par in zip(a, b) for num in par]
print(c)