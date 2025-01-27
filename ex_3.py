'''Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
números inteiros e retorne a soma total dos números.
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: 10'''

from functools import reduce


list_num = input('Digite os números separados por virgulas: ').split(',')
list_convert = [int(n) for n in list_num]

def sum_list():
    sum_number = reduce(
        lambda n, x : n + x,
        list_convert
    )
    return sum_number

print(sum_list())