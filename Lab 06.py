def main() -> None:
    # ENTRADAS
    entrada_1 = input()
    vetor1 = [int(numero) for numero in entrada_1.split(',')]

    entrada_2 = str(input())

    while entrada_2 != 'fim':

        # DEFININDO OPERACOES COM FUNCOES
        if entrada_2 == 'soma_vetores':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = soma_vetores(vetor1, vetor2)
            print(vetor1)

        elif entrada_2 == 'subtrai_vetores':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = subtrai_vetores(vetor1, vetor2)
            print(vetor1)

        elif entrada_2 == 'multiplica_vetores':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = multiplica_vetores(vetor1, vetor2)
            print(vetor1)

        elif entrada_2 == 'divide_vetores':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = divide_vetores(vetor1, vetor2)
            print(vetor1)

        elif entrada_2 == 'multiplicacao_escalar':
            entrada_3 = input()
            escalar = int(entrada_3)
            vetor1 = multiplicacao_escalar(vetor1, escalar)
            print(vetor1)

        elif entrada_2 == 'n_duplicacao':
            entrada_3 = input()
            escalar = int(entrada_3)
            vetor1 = n_duplicacao(vetor1, escalar)
            print(vetor1)

        elif entrada_2 == 'soma_elementos':
            vetor1 = [soma_elementos(vetor1)]
            print(vetor1)

        elif entrada_2 == 'produto_interno':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = [produto_interno(vetor1, vetor2)]
            print(vetor1)

        elif entrada_2 == 'multiplica_todos':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = multiplica_todos(vetor1, vetor2)
            print(vetor1)

        elif entrada_2 == 'correlacao_cruzada':
            entrada_3 = input()
            vetor2 = [int(numero) for numero in entrada_3.split(',')]
            vetor1 = correlacao_cruzada(vetor1, vetor2)
            print(vetor1)

        entrada_2 = str(input())

    if entrada_2 == 'fim':
        exit()


# DEFININDO FUNCAO SOMA
def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Retorna um vetor resultante da soma dos elementos de posicao i do
    primeiro vetor com os de mesma posicao do segundo vetor'''

    if len(vetor1) < len(vetor2):
        while len(vetor1) < len(vetor2):
            vetor1.append(0)
    elif len(vetor1) > len(vetor2):
        while len(vetor1) > len(vetor2):
            vetor2.append(0)
    vetor_zip = zip(vetor1, vetor2)
    soma = [a + b for a, b in vetor_zip]
    return soma


# DEFININDO FUNCAO SUBTRACAO
def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Retorna um vetor resultante da subtracao dos elementos de posicao i do
    primeiro vetor com os de mesma posicao do segundo vetor'''

    if len(vetor1) < len(vetor2):
        while len(vetor1) < len(vetor2):
            vetor1.append(0)
    elif len(vetor1) > len(vetor2):
        while len(vetor1) > len(vetor2):
            vetor2.append(0)
    vetor_zip = zip(vetor1, vetor2)
    subtracao = [a - b for a, b in vetor_zip]
    return subtracao


# DEFININDO FUNCAO MULTIPLICACAO
def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Retorna um vetor resultante da multiplicacao dos elementos de posicao
    i do primeiro vetor com os de mesma posicao do segundo vetor'''

    if len(vetor1) < len(vetor2):
        while len(vetor1) < len(vetor2):
            vetor1.append(1)
    elif len(vetor1) > len(vetor2):
        while len(vetor1) > len(vetor2):
            vetor2.append(1)
    vetor_zip = zip(vetor1, vetor2)
    multiplicacao = [a * b for a, b in vetor_zip]
    return multiplicacao


# DEFININDO FUNCAO DIVISAO
def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Retorna um vetor resultante da divisao dos elementos de posicao i do
    primeiro vetor com os de mesma posicao do segundo vetor'''

    if len(vetor1) < len(vetor2):
        while len(vetor1) < len(vetor2):
            vetor1.append(0)
    elif len(vetor1) > len(vetor2):
        while len(vetor1) > len(vetor2):
            vetor2.append(1)
    vetor_zip = zip(vetor1, vetor2)
    divisao = [a // b for a, b in vetor_zip]
    return divisao


# DEFININDO FUNCAO MULTIP POR ESCALAR
def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    '''Retorna um vetor com todos os elementos de um vetor
    multiplicados por um numero escalar'''

    vetor_multiplicado = []
    for elemento in vetor:
        vetor_multiplicado.append(elemento * escalar)
    return vetor_multiplicado


# DEFININDO FUNCAO DUPLICAR
def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    '''Retorna um novo vetor repetindo o vetor inicial n vezes'''

    i = 0
    vetor_duplicado = []
    while i < n:
        for k in range(len(vetor)):
            vetor_duplicado.append(vetor[k])
        i += 1
    return vetor_duplicado


# DEFININDO FUNCAO SOMA DE ELEMENTOS
def soma_elementos(vetor: list[int]) -> int:
    '''Retorna a soma todos os elementos de um vetor'''

    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma


# DEFININDO FUNCAO PRODUTO INTERNO
def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    '''Retorna a soma das multiplicacoes realizadas entre
        elementos de mesma posicao do vetor 1 e do vetor 2'''

    if len(vetor1) < len(vetor2):
        while len(vetor1) < len(vetor2):
            vetor1.append(1)
    elif len(vetor1) > len(vetor2):
        while len(vetor1) > len(vetor2):
            vetor2.append(1)
    vetor_zip = zip(vetor1, vetor2)
    resultado = [a * b for a, b in vetor_zip]
    return soma_elementos(resultado)


# DEFININDO FUNCAO MULTIPLICA TODOS
def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Retorna a soma da multiplicacao de cada elemento
        do primeiro vetor por todos os elementos
        do segundo vetor'''

    soma_vetor2 = soma_elementos(vetor2)
    return multiplicacao_escalar(vetor1, soma_vetor2)


# DEFININDO FUNCAO CORRELACAO CRUZADA
def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    ''' Realiza o produto interno utilizando um vetor e uma mascara, que é um
        vetor menor que caminha sobre o vetor maior, limitando as operacoes
        para os indices i contido no intervalo
        [0, tamanho do vetor - tamanho da mascara] '''

    resultado = []
    if len(vetor) >= len(mascara):
        for margem in range((len(vetor) - len(mascara)) + 1):
            elemento_resultado = 0
            for i in range(len(mascara)):
                elemento_resultado += vetor[i + margem] * mascara[i]
            resultado.append(elemento_resultado)
    return resultado


if __name__ == "__main__":
    main()