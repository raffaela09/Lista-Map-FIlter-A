'''Escreva uma função que receba uma lista de números inteiros e utilize lambda e
filter para dividir a lista em números pares e ímpares. Retorne um dicionário com
duas chaves: "pares" e "ímpares".
Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Exemplo de saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]}'''
list_numbers = input('Digite os números separados por virgula: ').split(',')
list_convert = [int(n) for n in list_numbers]

def numbers_even_not_even():
    even = list(
        filter(
            lambda n: n % 2 == 0,
            list_convert
        )
    )
    not_even = list(
        filter(
            lambda n: n % 2 !=0,
            list_convert
        )
    )
    
    even_not_even = {
        'Pares': even,
        'Impares': not_even,
    }
    return even_not_even

print(numbers_even_not_even())