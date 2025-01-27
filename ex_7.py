'''Escreva uma função que receba uma lista de números inteiros e utilize map e filter
para criar um dicionário que agrupe os números em três categorias:
o "positivos" (números maiores que 0)
o "negativos" (números menores que 0)
o "zeros" (números iguais a 0).
o Exemplo de entrada: [1, -2, 0, 3, -5, 0]
o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}'''

list_number = input('Digite os numeros separados por virgula: ').split(',')
list_convert = [int(n) for n in list_number]

def negative_or_positive():
    positive = list(
        filter(
            lambda n: n > 0,
            list_convert
        )
    )
    negative = list(
        filter(
            lambda n: n < 0, 
            list_convert
        )
    )
    zero = list(
        filter(
            lambda n: n == 0,
            list_convert
        )
    )
    positive_negative_zero = {
        'Positivos': positive,
        'Negativos': negative,
        'Zeros': zero
    }
    return positive_negative_zero

print(negative_or_positive())
#o map é dispensavel nesse caso.