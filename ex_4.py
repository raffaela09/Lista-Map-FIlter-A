'''Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
apenas os nomes com mais de 5 letras.
Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
Exemplo de saída: ["Lucas", "Fernanda"]'''

list_name = input('Digite os nomes separados por virgulas: ').split(',')

def names_than_five():
    names = list(
        filter(
            lambda name: len(name) >= 5,#mais ou igual a 5 letras? caso seja somente mais de 5 letras, basta retirar o igual, mas para a saída deseja é necessário ter o igual
            list_name
        )
    )
    return names

print(names_than_five())