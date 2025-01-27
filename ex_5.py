'''Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando
map, e depois retorne a lista ordenada.
Exemplo de entrada: [3, 1, 4, 2]
Exemplo de saída: [1, 4, 9, 16]'''
list_numbers = input('Digite os números separados por virgula: ').split(',')
list_convert = [int(n) for n in list_numbers]

def square_numbers():
    numbers = list(
        map(
            lambda n: n*n,
            list_convert
        )
    )
    return f'O quadrado dos números digitados são: {sorted(numbers)}'

print(square_numbers())