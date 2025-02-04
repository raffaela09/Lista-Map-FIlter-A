'''Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores
seja maior que 5.
Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)]
Exemplo de saída: [(2, 8), (4, 5, 6)]'''

lista = [(2, 8), (4, 5, 6), (1, 2)] #receber de input? 

def sum_tuple():
    conta = list(map(
            lambda n:n,
            lista
        ))#o uso do map nesse caso n é necessário, mas ja que no enunciado pede para utilizar
    filtro = list(
        filter(
            lambda n: sum(n)/2 >= 5, #maior que 5 ou maior ou igual a 5? casp seja somente maior que cinco, é só tirar o igual.
            conta
        )
    )
    
    return filtro

print(sum_tuple())