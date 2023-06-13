import random
import string

alfabeto = string.ascii_uppercase
vet = sorted([random.choice(alfabeto) for _ in range(128)])
left = 0
right = len(vet) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if vet[mid] == "K":
        found = True
        break
    elif vet[mid] < "K":
        left = mid + 1
    else:
        right = mid - 1

if found:
    print(f"O vetor é {vet}")
    print(f"Índice: {mid}")
else:
    print(f"Não existe a letra K no vetor")
    print(f"Vetor: {vet}")

