'''Crie uma função que receba um dicionário onde as chaves são nomes de alunos e
os valores são listas de notas (com pesos na última posição). A função deve calcular
a média ponderada de cada aluno usando reduce e retornar um novo dicionário
com os resultados.
Exemplo de entrada:
{
 "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
 "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}'''
from functools import reduce

dicionary = {
 'João': [8,7,9,2],
 'Ana': [5,6,7,3]
}

def calcular_media(dicionario, nome):
    last_item = dicionario[nome][-1]
    
    mult_last_item = list(map(
        lambda n: n * last_item,
        dicionario[nome]     
    ))
    mult_item_copy = mult_last_item.copy()
    mult_item_copy.pop(-1)
    divide = last_item * len(mult_item_copy)
    soma = reduce(
        lambda x,y: x+y,
        mult_item_copy
    )
    
    return soma / divide
    
media_joao = calcular_media(dicionary, 'João')
media_ana = calcular_media(dicionary, 'Ana')

dicionary_media = {
    'João': media_joao,
    'Ana': media_ana,
}
print(dicionary_media)

