massa_inicial = float(
    input("Informe a massa inicial em Kg de um material radioativo: ")
)
massa_inicial = massa_inicial * 1000
tempo = 0
massa_final = None
while massa_inicial > 0.5:
    massa_final = massa_inicial / 2
    tempo += 50
