'''Escreva uma função que, utilizando map e uma função lambda, receba uma lista
de números inteiros e retorne uma nova lista com todos os elementos dobrados.
Exemplo de entrada: [1, 2, Exemplo de saída: [2, 4, 6, 8]'''

list_numbers = input('Digite os numeros separados por virgulas:').split(',')
list_numbers_num = [int(n) for n in list_numbers]
def numbers_double():
    list_double = list(
        map(
            lambda n: n*2,
            list_numbers_num
        )
    )
    return f'O dobro dos números digitados são: {list_double}'

print(numbers_double())