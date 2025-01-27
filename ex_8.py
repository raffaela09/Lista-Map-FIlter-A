'''Crie uma função que receba uma lista de palavras e retorne a soma total de letras
em todas as palavras, utilizando map para contar as letras e reduce para somar.
Exemplo de entrada: ["casa", "python", "lambda"]
Exemplo de saída: 16'''
from functools import reduce


list_words = input('Digite as palavras separadas por virgula: ').split(',')

def count_letters():
    count = list(
        map(
            lambda n: len(n),
            list_words
        )
    )
    soma = reduce(
        lambda n,m: n+m,
        count
    )
    
    return soma

print(count_letters())