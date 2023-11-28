# Exercício 1

dict_1 = {
    "a": 1,
    "b": 2,
    "c": 5,
    "d": 9,
}

dict_2 = {
    "a": 10,
    "b": 1,
    "c": 4,
    "d": 1,
}


def merge_dict(dict_1: dict, dict_2: dict) -> dict:
    result = {}
    for key, value in dict_1.items():
        if key in dict_2.keys():
            result[key] = value + dict_2[key]
            
        else:
            result[key] = value
        
    for key, value in dict_2.items():
        if key not in dict_1.keys():
            result[key] = value
    return result


print(merge_dict(dict_1, dict_2))


# Exercício 2

dict_of_dicts = {
    'chave1': {'subchave1': 10, 'subchave2': 20},
    'chave2': {'subchave3': 30, 'subchave4': 25},
    'chave3': {'subchave5': 15, 'subchave6': 35}
}


def high_value_in_dicts(dict_of_dicts: dict) -> dict:
    high_value = float('-inf') 
    high_value_key = None
    result_high_value = None
    
    for key, dict in dict_of_dicts.items():
        for _, value in dict.items():
            if value > high_value:
                high_value = value
                high_value_key = key
                result_high_value = value

    print(f"A key com o maior value é '{high_value_key}' e o value é '{result_high_value}'.")


high_value_in_dicts(dict_of_dicts)

dicts = {
    "foods" : ["banana", "apple", "apple"],
    "animal": ["dog", "dog", "cat"],
    "names": ["gustavo", "gustavo", "thiago", "thiago", "kubiack"]
}

# Exercício 3

def unique_words(dictionary_of_lists: dict) -> dict:
    unique_words_per_key = {}

    for key, word_list in dictionary_of_lists.items():
        unique_words = []
        word_count = {}

        for word in word_list:
            word_count[word] = word_count.get(word, 0) + 1

        for word, occurrences in word_count.items():
            if occurrences == 1: 
                unique_words.append(word)

        unique_words_per_key[key] = unique_words

    for key, unique_words in unique_words_per_key.items():
        print(f"Unique words for '{key}': {unique_words}")


unique_words(dicts)

# Exercício 4

def create_nested_dictionary(keys_list, value):
    nested_dict = {}
    current_level = nested_dict

    for key in keys_list[:-1]:
        current_level = current_level.setdefault(key, {})
    
    current_level[keys_list[-1]] = value

    return nested_dict

keys = ['A', 'B', 'C']
value = 'Valor final'
nested_dict = create_nested_dictionary(keys, value)
print(nested_dict)


# Exercício 5

value_dict = {'a': 4, 'b': 5, 'c': 9}
value_dict['d'] = value_dict['a']
print(value_dict)


# Exercício 6

values = {
    11 : "a",
    21 : "b",
    32 : "c",
    43 : "d",
}
def dict_comprehension(values: dict, limit : int) -> dict:
    values = values.copy()
    for key in list(values.keys()):
        if key < limit:
            del values[key]
    return values

print(dict_comprehension(values, 13))


# Exercício 7

text = "Maça, Banana, Maça, Banana, Cachorro, Cachorro, Cachorro, Carro, Carro, Mouse"


def count(text: str) -> dict:
    words = text.split()
    result = {}
    for word in words:
        result[word] = words.count(word)
    return result


print(count(text))


# Exercício 8

def order_dict(values : dict) -> dict:
    sorted_list =  sorted(values.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_list}
    return sorted_dict

print(order_dict(values))

# Exercício 9

matrix_dictionary = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3,
    (1, 0): 4, (1, 1): 5, (1, 2): 6,
    (2, 0): 7, (2, 1): 8, (2, 2): 9
}

print(matrix_dictionary[0, 2])

# Exercício 10

replace_dict = {
    "php": "python",
    "odeio": "amo"
}

text = "eu odeio programar em php"

def replace(replace_dict: dict, text : str) -> str:
    for key in replace_dict.keys():
        text = text.replace(key, replace_dict[key])
    return text

print(replace(replace_dict, text))