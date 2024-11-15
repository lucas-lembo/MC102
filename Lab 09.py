def main():
    comodo = []
    n_linhas = int(input())
    for i in range(n_linhas):
        comodo.append(input().split(' '))
    anda_robo(comodo, n_linhas)


def anda_robo(comodo, linhas):
    '''
    Dada uma matriz que representa um comodo, determina que um robo ande da
    esquerda para a direita em linhas pares e que o mesmo ande da direita 
    para a esquerda em linhas impares.
    '''
    for i in range(linhas):
        if i % 2 == 0:
            for j in range(len(comodo[0])):
                coord_atual = [i, j]
                comodo[i][j] = 'r'
                if j != 0:
                    comodo[i][j - 1] = '.'
                elif i != 0 and j == 0:
                    comodo[i - 1][j] = '.'
                if i != 0 or j != 0:
                    print()
                imprime_comodo(comodo)
                sujeira = True
                sujeira = escaneia(comodo, sujeira, coord_atual)
                if sujeira:
                    if j + 1 < len(comodo[0]):
                        if comodo[i][j + 1] == 'o':
                            continue
                    elif i + 1 < len(comodo) and comodo[i + 1][len(comodo[0]) - 1] == 'o':
                        continue
                while sujeira:
                    comodo, coord_atual = limpa(comodo, coord_atual, i, j)
                    sujeira = escaneia(comodo, sujeira, coord_atual)
                comodo, coord_atual = retorna_posicao(comodo, i, j, coord_atual)

        elif i % 2 != 0:
            for j in range(len(comodo[0]) - 1, -1, -1):
                coord_atual = [i, j]
                comodo[i][j] = 'r'
                if j != (len(comodo[0]) - 1):
                    comodo[i][j + 1] = '.'
                else:
                    comodo[i - 1][j] = '.'
                print()
                imprime_comodo(comodo)
                sujeira = escaneia(comodo, sujeira, coord_atual)
                if sujeira:
                    if j - 1 >= 0:
                        if comodo[i][j - 1] == 'o':
                            continue    
                    elif i + 1 < len(comodo) and comodo[i + 1][0] == 'o':
                        continue
                while sujeira:
                    comodo, coord_atual = limpa(comodo, coord_atual, i, j)
                    sujeira = escaneia(comodo, sujeira, coord_atual)
                comodo, coord_atual = retorna_posicao(comodo, i, j, coord_atual)

            if i == (len(comodo) - 1):
                for j in range(1, len(comodo[0])):
                    coord_atual = [i, j]
                    comodo[i][j] = 'r'
                    comodo[i][j - 1] = '.'
                    print()
                    imprime_comodo(comodo)
                sujeira = escaneia(comodo, sujeira, coord_atual)
                if sujeira:
                    if j - 1 >= 0:
                        if comodo[i][j - 1] == 'o':
                            continue    
                    elif i + 1 < len(comodo) and comodo[i + 1][0] == 'o':
                        continue
                while sujeira:
                    comodo, coord_atual = limpa(comodo, coord_atual, i, j)
                    sujeira = escaneia(comodo, sujeira, coord_atual)

                comodo, coord_atual = retorna_posicao(comodo, i, j, coord_atual)


def escaneia(comodo, sujeira, coord_atual):
    '''
    Verifica se há sujeira em posicoes adjascentes ao robo na seguinte
    ordem: esquerda, cima, direita, baixo.
    '''
    if (coord_atual[1] - 1 >= 0) and (comodo[coord_atual[0]][coord_atual[1] - 1] == 'o'):
        sujeira = True
        return sujeira
    elif (coord_atual[0] - 1 >= 0) and (comodo[coord_atual[0] - 1][coord_atual[1]] == 'o'):
        sujeira = True
        return sujeira
    elif (coord_atual[1] + 1 < len(comodo[0])) and (comodo[coord_atual[0]][coord_atual[1] + 1] == 'o'):
        sujeira = True
        return sujeira
    elif (coord_atual[0] + 1 < len(comodo)) and (comodo[coord_atual[0] + 1][coord_atual[1]] == 'o'):
        sujeira = True
        return sujeira
    else:
        sujeira = False
        return sujeira


def limpa(comodo, coord_atual, i, j):
    '''
    Após realizar escaneamento, faz com que o robo 'r' limpe as posicoes adjascentes
    com sujeiras 'o', na seguinte sequencia: esquerda, cima, direita, baixo.
    '''
    if (coord_atual[1] - 1 >= 0) and (comodo[coord_atual[0]][coord_atual[1] - 1] == 'o'):
        comodo[coord_atual[0]][coord_atual[1] - 1] = 'r'
        comodo[coord_atual[0]][coord_atual[1]] = '.'
        coord_atual[1] -= 1
        print()
        imprime_comodo(comodo)
    elif (coord_atual[0] - 1 >= 0) and (comodo[coord_atual[0] - 1][coord_atual[1]] == 'o'):
        comodo[coord_atual[0] - 1][coord_atual[1]] = 'r'
        comodo[coord_atual[0]][coord_atual[1]] = '.'
        coord_atual[0] -= 1
        print()
        imprime_comodo(comodo)
    elif (coord_atual[1] + 1 < len(comodo[0])) and (comodo[coord_atual[0]][coord_atual[1] + 1] == 'o'):
        comodo[coord_atual[0]][coord_atual[1] + 1] = 'r'
        comodo[coord_atual[0]][coord_atual[1]] = '.'
        coord_atual[1] += 1
        print()
        imprime_comodo(comodo)
    elif (coord_atual[0] + 1 < len(comodo)) and (comodo[coord_atual[0] + 1][coord_atual[1]] == 'o'):
        comodo[coord_atual[0] + 1][coord_atual[1]] = 'r'
        comodo[coord_atual[0]][coord_atual[1]] = '.'
        coord_atual[0] += 1
        print()
        imprime_comodo(comodo)

    return comodo, coord_atual


def retorna_posicao(comodo, i, j, coord_atual):
    '''
    Faz com que o robo 'r' retorne da posicao que parou ao encerrar a sequencia de
    limpezas de 'o's até a posicao que iniciou o modo de limpeza.
    '''
    while coord_atual != [i, j]:
        if coord_atual[1] < j: 
            comodo[coord_atual[0]][coord_atual[1] + 1] = 'r'
            comodo[coord_atual[0]][coord_atual[1]] = '.'
            print()
            imprime_comodo(comodo)
            coord_atual = [coord_atual[0], coord_atual[1] + 1]
          
        if coord_atual[1] > j:
            comodo[coord_atual[0]][coord_atual[1] - 1] = 'r'
            comodo[coord_atual[0]][coord_atual[1]] = '.'
            print()
            imprime_comodo(comodo)
            coord_atual = [coord_atual[0], coord_atual[1] - 1]

        if coord_atual[1] == j:
            if coord_atual[0] > i:
                comodo[coord_atual[0] - 1][coord_atual[1]] = 'r'
                comodo[coord_atual[0]][coord_atual[1]] = '.'
                print()
                imprime_comodo(comodo)
                coord_atual = [coord_atual[0] - 1, coord_atual[1]]
            
    return comodo, coord_atual


def imprime_comodo(comodo):
    '''
    Imprime a matriz que representa o comodo.
    '''
    for n in range(len(comodo)):
        print(' '.join(comodo[n]))


if __name__ == '__main__':
    main()