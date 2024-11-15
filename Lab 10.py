
def main():
    # PONTOS DE VIDA ALOY
    a = int(input()) 
    a_max = a

    # FLECHAS E QUANTIDADES
    input_flechas = input().split(' ') 
    
    # ARMAZENANDO DADOS FLECHAS
    tipos_flechas = {}
    for i in range(0, len(input_flechas), 2):
        tipos_flechas[input_flechas[i]] = int(input_flechas[i + 1])

    # NUMERO DE MONSTROS
    n_monstros = int(input())
    combate = 0

    # COMBATES
    while n_monstros != 0 and a > 0:
        print(f'Combate {combate}, vida = {a}')
        flechas_usadas = {}
        # QTD MAQUINAS POR COMBATE
        qtd_maquinas = int(input())

        # CRIANDO O DICIONARIO DE ARMAZEAMENTO DE DADOS
        caracts_robos = ['P.V.', 'P.A.', 'PARTES']
        maquinas = {}
        for i in range(qtd_maquinas):
            maqs_print = []
            flechas_print = []
            maquina = {}
            dados_maquinas = input().split(' ')
            for j in range(len(dados_maquinas)):
                dados_maquinas[j] = int(dados_maquinas[j])
            for elemento in caracts_robos:
                maquina[elemento] = dados_maquinas[caracts_robos.index(elemento)]
            maquinas[i] = maquina

            # ADICIONANDO CARACTS DAS PARTES
            caracts_partes = ['fraqueza', 'dano_max', 'pt_critico']
            dict_partes = {}
            crits_receb = {}
            for j in range(dados_maquinas[2]):
                infos_parte = input().split(', ')
                parte = {}
                for k in range(len(caracts_partes)):
                    if k == 0:
                        parte[caracts_partes[k]] = infos_parte[k + 1]
                    elif k == 1:
                        parte[caracts_partes[k]] = int(infos_parte[k + 1])
                    elif k == 2:
                        parte[caracts_partes[k]] = (int(infos_parte[k + 1]), (int(infos_parte[k + 2])))
                    elif k == 3:
                        parte[caracts_partes[k]] = crits_receb
                dict_partes[infos_parte[0]] = parte
            maquina['PARTES'] = dict_partes

        # CONTABILIZANDO ACERTOS E DANOS
        tem_flechas = True
        tem_inimigos = True
        criticos = {}
        while tem_flechas and tem_inimigos and (a > 0):
            # UNIDADE, PARTE, TIPO FLECHA, COORD X, COORD Y 3x 
            n = 0
            while n < 3:
                resta_inimigos = inimigos_restantes(maquinas)
                if resta_inimigos == False:
                    break
                elif resta_inimigos:
                    ataque = input().split(', ')
                    if int(ataque[0]) not in maqs_print:
                        maqs_print.append(int(ataque[0]))
                    if ataque[2] not in flechas_print:
                        flechas_print.append(ataque[2])
                    maquinas, tipos_flechas = calcula_vida(maquinas, ataque, tipos_flechas)
                    flechas_usadas = calculo_flechas(ataque, tipos_flechas, flechas_usadas)
                    tem_flechas = sobrou_flechas_combate(tipos_flechas, flechas_usadas)
                    criticos = contagem_criticos(maquinas, ataque, criticos)
                n += 1
            
            # ALOY RECEBE DANO
            if tem_inimigos:
                dano_recebido = dano_aloy(maquinas)
                a -= dano_recebido
                if a < 0:
                    a = 0

            # MANTEM LOOP
            tem_flechas = sobrou_flechas_combate(tipos_flechas, flechas_usadas)
            tem_inimigos = inimigos_restantes(maquinas)

            if sobrou_flechas_combate(tipos_flechas, flechas_usadas) == False:
                print('Vida após o combate =', a)
                print('Aloy ficou sem flechas e recomeçará sua missão mais preparada.')
                exit()

        # PRINTS FINAL DO COMBATE
        print('Vida após o combate =', a)
        if a != 0:
            print('Flechas utilizadas:')
            for flecha in sorted(flechas_usadas):
                print(f'- {flecha}: {flechas_usadas[flecha]}/{tipos_flechas[flecha]}')
            if len(criticos) != 0:
                print('Críticos acertados:')
                for maquina in sorted(criticos):
                    if len(criticos[maquina]):
                        print(f'Máquina {maquina}:')    
                        for ponto in criticos[maquina]:
                            print(f'- {ponto}: {criticos[maquina][ponto]}x')
        elif a == 0:
            print('Aloy foi derrotada em combate e não retornará a tribo.')
            break

        # ATUALIZANDO PARA O PROXIMO COMBATE
        if tem_inimigos == False:
            n_monstros -= qtd_maquinas
            if n_monstros <= 0:
                break
            combate += 1

        if a != a_max:
            if a + (a_max // 2) > a_max:
                a = a_max
            else:
                a = a + (a_max // 2)

    # PRINTS FINAIS  
    
    if tem_inimigos == False:
        print('Aloy provou seu valor e voltou para sua tribo.')


def sobrou_flechas(tipos):
    '''
    Retorna true se ainda há flechas restantes e retorna
    false se as flechas acabaram.
    '''
    quantidade = list(tipos.values())
    flechas_rest = soma_elementos(quantidade)
    if flechas_rest == 0:
        return False
    elif flechas_rest != 0:
        return True


def inimigos_restantes(maquinas):
    '''
    Retorna true se ainda há algum inimigo com vida e retorna false se não
    há mais nenhum inimigo com vida.
    '''
    vida_maquinas = [maquina['P.V.'] for maquina in maquinas.values()]
    inimigos_restantes = soma_elementos(vida_maquinas)
    if inimigos_restantes == 0:
        return False
    elif inimigos_restantes != 0:
        return True


def soma_elementos(lista):
    '''
    Soma todos os elementos de uma lista.
    '''
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma


def calcula_vida(maquinas, ataque, flechas):
    '''
    Retorna os pontos vida de uma maquina inimiga apos um ataque de Aloy.
    '''
    dano = 0
    parte_atingida = maquinas[int(ataque[0])]['PARTES'][ataque[1]]
    
    # CALCULANDO DANO
    dano += parte_atingida['dano_max']
    if parte_atingida['pt_critico'] != (int(ataque[3]), int(ataque[4])):
        x = (parte_atingida['pt_critico'][0] - int(ataque[3]))
        if x < 0:
            x = -x
        y = ((parte_atingida['pt_critico'])[1] - int(ataque[4]))
        if y < 0:
            y = -y
        dano -= (x + y)
    if parte_atingida['fraqueza'] != 'todas':
        if parte_atingida['fraqueza'] != ataque[2] or parte_atingida['fraqueza'] == 'nenhuma':
            dano = dano // 2
    if dano < 0:
        dano = 0
    maquinas[int(ataque[0])]['P.V.'] -= dano
    if maquinas[int(ataque[0])]['P.V.'] <= 0:
        maquinas[int(ataque[0])]['P.V.'] = 0
    
    # PRINT MAQ DERROTADA
    if maquinas[int(ataque[0])]['P.V.'] == 0:
        print('Máquina', ataque[0], 'derrotada')
    return maquinas, flechas


def dano_aloy(maquinas):
    '''
    Retorna um inteiro correspondente ao dano sofrido por Aloy durante
    o combate
    '''
    dano = []
    for maquina in maquinas:
        if maquinas[maquina]['P.V.'] != 0:
            dano.append(maquinas[maquina]['P.A.'])
    return soma_elementos(dano)


def calculo_flechas(ataque, flechas_rest, flechas_usadas):
    '''
    Registra o a quantidade e o tipo de cada flecha utilizada por Aloy.
    '''
    if ataque[2] not in flechas_usadas:
        flechas_usadas[ataque[2]] = 0
    flechas_usadas[ataque[2]] += 1
    return flechas_usadas


def contagem_criticos(maquinas, ataque, criticos):
    '''
    Registra, em um dicionario, a coordenada e a ocorrencia de cada ponto critico recebido
    por cada maquina, se existir algum.
    '''
    parte_atingida = maquinas[int(ataque[0])]['PARTES'][ataque[1]]
    coord_acerto = (int(ataque[3]), int(ataque[4]))

    if parte_atingida['pt_critico'] == coord_acerto:
        if int(ataque[0]) not in criticos:
            criticos[int(ataque[0])] = {}
        if coord_acerto not in criticos[int(ataque[0])]:
            criticos[int(ataque[0])][coord_acerto] = 0
        criticos[int(ataque[0])][coord_acerto] += 1
    return criticos

def sobrou_flechas_combate(tipos_flechas, flechas_usadas):
    '''
    Retorna true se ainda há flechas restantes e retorna
    false se as flechas acabaram.
    '''
    if tipos_flechas == flechas_usadas:
        return False
    else:
        return True



if __name__ == '__main__':
    main()