def encontra_indice(mensagem: list[str], busca: str, inicio: int = 0) -> int:
    ''' Encontra o indice da busca desejada em uma mensagem '''

    vogais = 'aeiouAEIOU'
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    numeros = '1234567890'
    indice = 0
    if busca == 'vogal':
        for i in range(inicio, len(mensagem)):
            if mensagem[i] in vogais:
                indice = i
                break

    elif busca == 'consoante':
        for i in range(inicio, len(mensagem)):
            if mensagem[i] in consoantes:
                indice = i
                break

    elif busca == 'numero':
        for i in range(inicio, len(mensagem)):
            if mensagem[i] in numeros:
                indice = i
                break
    else:
        for i in range(inicio, len(mensagem)):
            if busca == mensagem[i]:
                indice = i
                break

    return indice


def aplica_operacao(numero1: int, numero2: int, operacao: str) -> int:
    ''' Determina qual operacao deve ser realizada entre dois numeros e

          fornece o resultado da operacao'''
    
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    return resultado


def traduz_mensagem(texto: list, numero: int) -> list[str]:
    ''' Substitui cada caractere de indice i de um texto por um de indice i + numero
     
        baseando-se na tabela ASCII. '''
    
    traducao = []
    for string in texto:
        linha_traducao = []
        for caractere in string:
            caractere_traducao = chr(ord(caractere) + numero)
            indice_final = ((ord(caractere) + numero) - 32) % 95 + 32
            caractere_traducao = chr(indice_final)
            linha_traducao.append(caractere_traducao)
        traducao.append(''.join(map(str, linha_traducao)))
    return traducao


def main():
    operacao_indice = input()
    busca_indice = [input().split() for _ in range(2)]
    n_linhas = int(input())
    mensagem = [input() for _ in range(n_linhas)]

    mensagem_unificada = []
    k = 0
    while k < n_linhas:
        mensagem_unificada += mensagem[k]
        k += 1

    indice_1 = encontra_indice(mensagem_unificada, busca_indice[0][0])

    indice_2 = encontra_indice(
        mensagem_unificada, busca_indice[1][0], indice_1
    )

    chave = aplica_operacao(indice_1, indice_2, operacao_indice)

    texto_traducao = traduz_mensagem(mensagem, chave)

    print(chave)
    for linha in texto_traducao:
        print(linha)


if __name__ == "__main__":
    main()