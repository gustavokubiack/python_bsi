# Exercício 1

with open("arquivos/texto.txt", "w") as f:
    f.write("Olá mundo!")
    f.close()

# Exercício 2

with open("arquivos/texto.txt") as f:
    print(f.read())

# Exercício 3

with open("arquivos/texto.txt") as f:
    count = 0
    for line in f.readlines():
        count += 1
    print(f"O número de linhas é: {count}")

# Exercício 4

with open("arquivos/texto.txt") as f:
    text = f.read()
with open("arquivos/copia.txt", "w") as f:
    f.write(text)

# Exercício 5

with open("arquivos/texto.txt") as f:
    text = f.read()
with open("arquivos/copia.txt") as f:
    copy = f.read()
with open("arquivos/combinado.txt", "w") as f:
    text += "\n"
    f.write(text)
    f.write(copy)

# Exercício 6

with open("arquivos/texto.txt") as f:
    lines = [line for line in f.readlines()]
    words = [word for line in lines for word in line.split()]
    print(f"A quantidade de palavras é: {len(words)}")

# Exercício 7
with open("arquivos/texto.txt") as f:
    text = f.read()
    phrase = text.replace("mundo", "Python")
with open("arquivos/modificado.txt", "w") as f:
    f.write(phrase)

# Exercício 8
with open("arquivos/texto.txt", "a") as f:
    phrase = "\nIsso é incrível!"
    f.write(phrase)

# Exercício 9

with open("arquivos/texto.txt") as f:
    lines = [line for line in f.readlines()]
    words = [word for line in lines for word in line.split()]
    count = 0
    for letter in words:
        count += len(letter)
    print(f"A quantidade de letras no texto.txt é: {count}")


# Exercício 10
with open("arquivos/numeros.txt", "w") as f:
    for line in range(0, 101):
        if line < 100:
            f.write(f"{line},")
        else:
            f.write(f"{line}")

with open("arquivos/numeros.txt") as f:
    lines = f.read()
    numbers = [int(number) for number in lines.split(",")]
    print(f"A soma de 0 a 100 é: {sum(numbers)}")


# Exercício 11

valid = []
invalid = []

with open("arquivos/ips.txt") as f:
    for ip in f.readlines():
        ip = ip.strip()

        octets = ip.split(".")
        if len(octets) != 4:
            invalid.append(ip)
            continue 

        valid_ip = True
        for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                invalid.append(ip)
                valid_ip = False
                break 

        if valid_ip:
            valid.append(ip)

print("Endereços IP válidos:")
print(valid)
print("\nEndereços IP inválidos:")
print(invalid)


# Exercício 12

def storage_used(bytes):
    return round(int(bytes) / (1024 * 1024), 2)


def storage_percentage(users_storage):
    total = sum(users_storage)
    percentages = []
    for user in users_storage:
        percentage = user * 100 / total
        percentages.append(round(percentage, 6))
    return percentages


with open("arquivos/usuarios.txt") as f:
    users_storage = []
    names = []
    for user in f.readlines():
        user = user.replace("\t", " ").split()
        names.append(user[0])
        user_storage = storage_used(user[1])
        users_storage.append(user_storage)

with open("arquivos/relatorios.txt", "w") as f:
    f.write("Nr.\tUsuário\t\tEspaço Utilizado\tPorcentagem de uso\n")
    for index, (name, storage) in enumerate(zip(names, users_storage), start=1):
        percentage = storage_percentage(users_storage)[index - 1]
        storage = f"{str(storage)} MB"
        storage = storage.replace(".", ",")
        f.write(f"{index}\t{name.capitalize().ljust(10)}\t{storage.ljust(25)}\t{str(percentage)}%\n")


# Exercício 13

def paginate_file(input_file, output_file):
    lines_per_page = 60
    characters_per_line = 76

    with open(input_file, 'r') as file_input:
        lines = file_input.readlines()

    pages = []
    current_page = []
    page_number = 1

    for line in lines:
        while len(line) > characters_per_line:
            current_page.append(line[:characters_per_line])
            line = line[characters_per_line:]
        current_page.append(line)

        if len(current_page) >= lines_per_page:
            pages.append(current_page)
            current_page = []
            page_number += 1

    if current_page:
        pages.append(current_page)

    with open(output_file, 'w') as file_output:
        for index, page in enumerate(pages, start=1):
            file_output.write(f"Página {index} - Arquivo: {input_file}\n")
            file_output.write('\n'.join(page))
            file_output.write(f"Página {index} - Arquivo: {output_file}\n\n")


input_file_name = 'arquivos/entrada.txt'
output_file_name = 'arquivos/saida.txt'

paginate_file(input_file_name, output_file_name)



# Exercício 14

def clean_file(input_file, output_file):
    cleaned_lines = []
    empty_line = False

    with open(input_file, 'r') as file_input:
        lines = file_input.readlines()

    for line in lines:
        line = line.strip()  

        if line:  
            cleaned_lines.append(' '.join(line.split()))  
            empty_line = False
        else:
            if not empty_line: 
                cleaned_lines.append('')
                empty_line = True

    with open(output_file, 'w') as file_output:
        file_output.write('\n'.join(cleaned_lines))

    print(f"Cleaned file created: {output_file}")


input_file_name = 'arquivos/entrada_suja.txt'
output_file_name = 'arquivos/saida_limpa.txt'

clean_file(input_file_name, output_file_name)
