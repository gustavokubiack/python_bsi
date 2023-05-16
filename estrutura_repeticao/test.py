diarias = int(input("Informe o número de diárias: "))

if diarias < 15:
    taxa = 7.5
elif diarias == 15:
    taxa = 6.5
else:
    taxa = 5

print(f"Valor total a pagar: {(diarias * 50) + (diarias * taxa)}")