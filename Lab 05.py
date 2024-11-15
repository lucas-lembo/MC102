genoma_atual = input()

def main():
    funcao = input().split()
    while funcao != 'sair':
        if 'reverter'== funcao[0]:
            reverter(int(funcao[1]), int(funcao[2]))
        elif 'transpor' == funcao[0]:
            transpor(int(funcao[1]), int(funcao[2]), int(funcao[3]))
        elif 'combinar' == funcao[0]:
            combinar(funcao[1], int(funcao[2]))
        elif 'concatenar' == funcao[0]:
            concatenar(funcao[1])
        elif 'remover' == funcao[0]:
            remover(int(funcao[1]), int(funcao[2]))
        elif 'transpor_e_reverter' == funcao[0]:
            transp_rev(int(funcao[1]), int(funcao[2]), int(funcao[3]))
        elif 'buscar' == funcao[0]:
            buscar(funcao[1])
        elif 'buscar_bidirecional' == funcao[0]:
            buscar_bid(funcao[1])
        elif 'mostrar' == funcao[0]:
            mostrar()
        elif funcao[0] == 'sair':
            exit()
        funcao = input().split()
    if funcao == 'sair':
        exit()


# DEFININDO FUNCAO REVERTER
def reverter(i, j):
    ''' Inverte a sequência de letras do intervalo de i até j '''
    
    global genoma_atual
    genoma_revertido = genoma_atual[:i] + genoma_atual[i:j + 1][::-1] + genoma_atual[j + 1:]
    genoma_atual = genoma_revertido
    

# DEFININDO FUNCAO TRANSPOR
def transpor(i, j, k):
    ''' Troca de posição os intervalos de i até j com o de j + 1 até k '''
    
    global genoma_atual
    genoma_transposto = genoma_atual[:i] + genoma_atual[j + 1:k + 1] + genoma_atual[i: j + 1] + genoma_atual[k + 1:]
    genoma_atual = genoma_transposto

# DEFINDO FUNCAO COMBINAR
def combinar(genoma_inserido, i):
    ''' Insere uma sequência de genomas na posição i do genoma atual '''

    global genoma_atual
    genoma_combinado = genoma_atual[:i] + genoma_inserido + genoma_atual[i:]
    genoma_atual = genoma_combinado


# DEFININDO FUNCAO CONCATENAR
def concatenar(genoma_final):
    ''' Adiciona uma sequência de genomas ao final do genoma atual '''

    global genoma_atual
    genoma_concatenado = genoma_atual[:] + genoma_final
    genoma_atual = genoma_concatenado


# DEFININDO FUNCAO REMOVER
def remover(i, j):
    ''' Remove a sequência que se inicia em i e termina em j do genoma atual '''

    global genoma_atual
    genoma_pos_remocao = genoma_atual[:i] + genoma_atual[j + 1:]
    genoma_atual = genoma_pos_remocao
    # CORRIGIR ! ! !



# DEFININDO FUNCAO TRANSPOR E REVERTER
def transp_rev(i, j, k):
    ''' Transpõe o intervalo de i até j com o intervalo de j + 1 até k
     
      e depois inverte a sequência de i até k '''
    
    global genoma_atual
    genoma_transp = genoma_atual[:i] + genoma_atual[j + 1:k + 1] + genoma_atual[i: j + 1] + genoma_atual[k + 1:]
    genoma_transp_rev = genoma_transp[:i] + genoma_transp[i:k + 1][::-1] + genoma_transp[k + 1:]
    genoma_atual = genoma_transp_rev


# DEFININDO FUNCAO BUSCAR
def buscar(genoma_busca):
    ''' Mostra quantas vezes a sequência digitada está presente no genoma atual
     
      apenas no sentido normal de leitura '''
    
    global genoma_atual
    print(genoma_atual.count(genoma_busca))
    # CORRIGIR ! ! !


# DEFININDO FUNCAO BUSCAR BIDIRECIONAL
def buscar_bid(genoma_busca):
    ''' Mostra quantas vezes a sequência digitada está presente no genoma atual

      tanto no sentido normal de leitura quanto no sentido invertido '''
    
    global genoma_atual
    print((genoma_atual.count(genoma_busca)) + genoma_atual.count(genoma_busca[::-1]))

# DEFININDO FUNCAO MOSTRAR
def mostrar():
    ''' Imprime o genoma atual '''
    
    global genoma_atual
    print(genoma_atual)

main()