'''Escreva uma função que, utilizando filter e uma função lambda, receba uma lista
de números inteiros e retorne apenas os números pares.
Exemplo de entrada: [1, 2, 3, 4, 5]
Exemplo de saída: [2, 4]'''

list_numbers = input('Digite os números separados por virgula: ').split(',')
list_convert = [int(n) for n in list_numbers]
def numbers_par():
    list_even = list(
        filter(
            lambda n: n %  2 == 0,
            list_convert
        )
    )
    return f'Os números pares são: {list_even}'

print(numbers_par())