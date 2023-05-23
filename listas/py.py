"""Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se
existirem, escrever as posições em que estão armazenados."""
todos_num = [float(input(f"Informe um número {num+1}: ")) for num in range(5)]
num_30 = [i for i, num in enumerate(todos_num) if num == 30]
print(num_30)


