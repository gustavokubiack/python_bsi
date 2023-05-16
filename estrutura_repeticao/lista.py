"""Faça um algoritmo que:
• leia 5 números inteiros;
• escreva os números que são negativos;
• escreva a média dos números positivos."""

media = []
for num in range(3):
    num = int(input("Digite um número: "))
    if num < 0:
        print(f"O número {num} é negativo.")
    else:
        num > 0
        media.append(num)
        print(f"O número {num} é positivo.")

print(f"A média dos números positivos é {sum(media)/len(media)}")


"""Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é
par ou ímpar."""

for num in range(16):
    num = int(input("Digite um número: "))
    if num % 2 == 0: 
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

"""Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos
números ímpares entre 1 e 100."""

par = []
impar = []
for num in range(101):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Soma dos números pares: {sum(par)}")
print(f"Soma dos números ímpares: {sum(impar)}")

"""Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das
alturas."""

alturas = []
for altura in range(21):
    altura = float(input("Informe a sua altura: "))
    alturas.append(altura)
print(f"A média das alturas é {sum(alturas)/len(alturas)}")

"""Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são
negativos."""

num_maior = int(input("Informe o maior valor: "))
num_menor = int(input("Informe o menor valor: "))
for num in range(num_menor, num_maior):
    if num_menor > num_maior:
        raise "Error"
    elif num < 0:
        print(f"{num}")

"""Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”.
Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui."""

quant_tinta = int(input("Informe a quantidade de tinta: "))
while quant_tinta != 0:
    quant_tinta += -2
    print("Tá escrevendo...")    

"""Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
• o número de inscrição e a altura do atleta mais alto;
• o número de inscrição e a altura do atleta mais baixo;
• a altura média do grupo de atletas."""

inscricoes = []
alturas = []

for i in range(3):
    inscricao = float(input("Informe a inscrição: "))
    altura = float(input("Informe a altura: "))
    inscricoes.append(inscricao)
    alturas.append(altura)

indice_mais_alto = alturas.index(max(alturas))
indice_mais_baixo = alturas.index(min(alturas))

inscricao_mais_alto = inscricoes[indice_mais_alto]
inscricao_mais_baixo = inscricoes[indice_mais_baixo]

print(f"Média das alturas: {sum(alturas) / len(alturas)}")
print(f"Atleta mais alto: Altura={max(alturas)}, Inscrição={inscricao_mais_alto}")
print(f"Atleta mais baixo: Altura={min(alturas)}, Inscrição={inscricao_mais_baixo}")

"""Construir um algoritmo que calcule o fatorial de um número N."""

fatorial = int(input("Informe um valor: "))
for num in range(1, fatorial):
    fatorial *= num
print(fatorial)

"""Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:"""

count = []
for num in range(1,101):
    count.append(num)
print(sum(count))


"""Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:"""
count = []
for num in range(1,101):
    a = 1/num
    count.append(a)
print(sum(count))

"""Faça um algoritmo para calular e escrever o valor de S, dado por:
S = 1/N + 2/N-1 + 3/N-2 + ... + N/1, semdo N fornecido pelo usuário."""

n = int(input("Informe um valor: "))
count = []
for num in range(1, n+1):
    a = num/(n+1-num)
    count.append(a)
print(sum(count))

"""Foi feita uma pesquisa de audiência de canal de TV em n casas de um determinado
bairro de Joinville, em um certo dia do mês. Na pesquisa foi utilizado um coletor de
dados portátil. Para cada casa visitada, foi fornecido o número do canal (4, 5, 9, 12) e
o número de pessoas que estavam assistindo a TV naquele horário, considerando que
em cada casa só existia uma televisão. Em casas onde a televisão estava desligada, foi
registrado zero para o número do canal e para o número de pessoas. Faça um
algoritmo que calcule e escreva, para cada emissora, o percentual de audiência."""

canal_4 = []
canal_5 = []
canal_9 = []
canal_12 = []

for num in range(3):
    canal = int(input("Informe o canal: "))
    if canal == 4:
        canal_4.append(canal)
    elif canal == 5:
        canal_5.append(canal)
    elif canal == 9:
        canal_9.append(canal)
    elif canal == 12:
        canal_12.append(canal)
    else:
        print("Canal inválido.")

print(f"Percentual de audiência do canal 4: {len(canal_4)/3}")
print(f"Percentual de audiência do canal 5: {len(canal_5)/3}")
print(f"Percentual de audiência do canal 9: {len(canal_9)/3}")
print(f"Percentual de audiência do canal 12: {len(canal_12)/3}")


"""Uma turma tem 50 alunos. Faça um algoritmo que:
• leia para cada aluno o seu nome e idade;
• escreva os nomes dos alunos que tem 18 anos;
• escreva a quantidade de alunos que tem idade acima de 20 anos."""

nomes_18 = []
nomes_20 = []

for aluno in range(3):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    if idade == 18:
        nomes_18.append(nome)
    elif idade > 20:
        nomes_20.append(nome)
    else:
        print("Idade inválida.")

print(f"Alunos com 18 anos: {nomes_18}")
print(f"Alunos com mais de 20 anos: {len(nomes_20)}")


"""Faça um algoritmo que:
• leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e
sexo = 'F' ou sexo = 'f' para feminino);
• escreva a média da altura das mulheres;
• escreva a média da altura da turma."""

alturas_turma = []
altura_mulheres = []

for pessoa in range(3):
    altura = float(input("Informe a altura: "))
    sexo = input("Informe o sexo: ")
    if sexo == "F" or sexo == 'f':
        altura_mulheres.append(altura)
    alturas_turma.append(altura)

print(f"Média da altura das mulheres: {sum(altura_mulheres)/len(altura_mulheres)}")
print(f"Média da altura da turma: {sum(alturas_turma)/len(alturas_turma)}")

"""Uma loja de departamentos oferece para seus clientes um determinado desconto de
acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra
seja maior que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que
leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar.
Um nome de cliente igual a ULTIMO indica o fim da entrada de dados."""

nome = None
while nome != "ULTIMO":
    nome = input("Informe o nome: ")
    endereco = input("Informe o endereço: ")
    valor_compra = float(input("Inform o valor da compra: "))
    if valor_compra > 500:
        valor_compra = valor_compra - (valor_compra * 0.2)
    else:
        valor_compra = valor_compra - (valor_compra * 0.15)
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco}")
    print(f"Valor da compra: {valor_compra}")


"""Faça um algoritmo que leia valores, sendo que cada valor representa a idade de uma
pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser
computados no cálculo valores maiores do que zero. O algoritmo deve apresentar ao
usuário a seguinte mensagem:
deseja digitar mais um valor: s (SIM) / n (NAO)?,
antes de prosseguir com a entrada de dados."""

idades = []

while True:
    idade = int(input("Informe a idade: "))
    if idade > 0:
        idades.append(idade)
    else:
        print("Idade inválida.")
    continuar = input("Deseja digitar mais um valor: s (SIM) / n (NAO)?")
    if continuar == "n":
        break

print(f"Idade média do grupo de pessoas: {sum(idades)/len(idades)}")

"""Um hotel cobra R$ 50,00 de diária por hóspede e mais uma taxa de serviços. A taxa de
serviços é de:
• R$ 7,50 por diária, caso o número de diárias seja menor que 15;
• R$ 6,50 por diária, caso o número de diárias seja igual a 15;
• R$ 5,00 por diária, caso o número de diárias seja maior que 15."""

diarias = int(input("Informe o número de diárias: "))

if diarias < 15:
    taxa = 7.5
elif diarias == 15:
    taxa = 6.5
else:
    taxa = 5

print(f"Valor total a pagar: {(diarias * 50) + (diarias * taxa)}")


