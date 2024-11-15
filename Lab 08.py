def main():
    # ENTRADAS
    num_filmes = int(input())
    lista_filmes = []
    for i in range(num_filmes):
        filme = input()
        lista_filmes.append(filme)
    num_avaliacoes = int(input())
    tot_avaliacoes = []
    categorias = []
    for i in range(num_avaliacoes):
        avaliacao = input().split(', ')
        tot_avaliacoes.append(avaliacao)
        if avaliacao[1] not in categorias:
            categorias.append(avaliacao[1])

    # ORGANIZACAO DE DICIONARIOS
    categorias_simples = {}
    for categoria in tot_avaliacoes:  # CRIANDO DICT DE CHAVE CATEGORIA
        filmes = {}
        for filme in lista_filmes:  # CRIANDO DICT DE CHAVE FILMES
            filmes[filme] = []
        categorias_simples[categoria[1]] = filmes

    # ADICIONANDO NOTAS
    for i in range(len(tot_avaliacoes)):
        categorias_simples[tot_avaliacoes[i][1]][tot_avaliacoes[i][2]].append(int(tot_avaliacoes[i][3]))

    # CALCULANDO MEDIAS
    categorias_simples_media = calcula_media(categorias_simples, categorias, lista_filmes)

    # DEFININDO VENCEDORES CATEGORIAS SIMPLES
    vencedores_cat_simples, cat_dos_venc = acha_win_cat_simples(categorias_simples_media, categorias_simples, categorias, lista_filmes)

    # VENCEDOR CATEGORIA PIOR DO ANO
    recorde_premios = 0
    maior_venc = ['maior_venc']
    for i in range(len(vencedores_cat_simples)):
        if vencedores_cat_simples.count(vencedores_cat_simples[i]) > recorde_premios:
            recorde_premios = vencedores_cat_simples.count(vencedores_cat_simples[i])
            maior_venc[0] = vencedores_cat_simples[i]
            soma_filme = 0
            for categoria in categorias:
                soma_filme += categorias_simples_media[categoria][vencedores_cat_simples[i]]
            desempate = soma_filme
        elif vencedores_cat_simples.count(vencedores_cat_simples[i]) == recorde_premios:
            soma_desempate = 0
            for categoria in categorias:
                soma_desempate += categorias_simples_media[categoria][vencedores_cat_simples[i]]
            if soma_desempate > desempate:
                maior_venc[0] = vencedores_cat_simples[i]
                desempate = soma_desempate

    ordem_categorias = ['filme que causou mais bocejos', 'filme que foi mais pausado', 
                        'filme que mais revirou olhos', 'filme que não gerou discussão nas redes sociais',
                        'enredo mais sem noção']
    categorias_especiais = ['prêmio pior filme do ano', 'prêmio não merecia estar aqui']

    # VENCEDOR CATEGORIA NAO MERECIA
    filmes_avaliados = []
    nao_avaliados = []
    for i in range(len(tot_avaliacoes)):
        if tot_avaliacoes[i][2] not in filmes_avaliados:
            filmes_avaliados.append(tot_avaliacoes[i][2])
    for filme in lista_filmes:
        if filme not in filmes_avaliados:
            nao_avaliados.append(filme)

    # SAIDAS
    print('#### abacaxi de ouro ####')
    print()
    print('categorias simples')

    for categoria in ordem_categorias:
        filme_printado = vencedores_cat_simples[cat_dos_venc.index(categoria)]
        print('categoria:', categoria)
        print('-', filme_printado)
    print()
    print('categorias especiais')

    for categoria in categorias_especiais:
        if categoria != 'prêmio não merecia estar aqui':
            print(categoria)
            print('-', maior_venc[0])
        else:
            print(categoria)
            if len(nao_avaliados) == 0:
                print('- sem ganhadores')
            else:
                print('-', ', '.join(nao_avaliados))


def calcula_media(dicionario, categorias, filmes):
    '''
    CALCULA A MEDIA ALCANÇADA POR CADA FILME EM CADA CATEGORIA
    BASEADA NAS NOTAS DADAS PELOS AVALIADORES
    '''
    dicionario_media = {}

    for categoria in categorias:
        dicionario_media[categoria] = {}
        for filme in filmes:
            soma = 0
            for i in dicionario[categoria][filme]:
                soma += i
            if len(dicionario[categoria][filme]) != 0:
                media = soma / len(dicionario[categoria][filme])
            elif len(dicionario[categoria][filme]) == 0:
                media = 0
            dicionario_media[categoria][filme] = media
    return dicionario_media


def acha_win_cat_simples(dict_medias, dict_notas, categorias, filmes):
    '''
    DETERMINA O VENCEDOR DE CADA CATEGORIA SIMPLES BASEANDO-SE EM CRITÉROS
    PRÉ DETERMINADOS
    '''
    vencedores = []
    categ_venc = []
    for categoria in categorias:
        vencedor_categoria = ['vencedor']
        categoria_do_vencedor = ['categoria']
        pont_max = 0
        for filme in filmes:
            if dict_medias[categoria][filme] > pont_max:
                pont_max = dict_medias[categoria][filme]
                vencedor_categoria[0] = filme
                categoria_do_vencedor[0] = categoria
            elif dict_medias[categoria][filme] == pont_max:
                if len(dict_notas[categoria][filme]) != 0:
                    if len(dict_notas[categoria][filme]) > len(dict_notas[categoria][vencedor_categoria[0]]):
                        vencedor_categoria[0] = filme
                        categoria_do_vencedor[0] = categoria
        vencedores.append(vencedor_categoria[0])
        categ_venc.append(categoria_do_vencedor[0])
    return vencedores, categ_venc


main()
