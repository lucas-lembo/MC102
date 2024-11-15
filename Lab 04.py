dias = int(input())
for l in range(1, dias + 1):
    n_brigas = int(input())
    
    possiveis_brigas = []
    for _ in range(n_brigas):
        a = input().split()
        possiveis_brigas.append(a)
    
    briguentos = []
    for lista in possiveis_brigas:
        briguentos += lista
    
    servicos_dia = input().split()

    
    for j in range(1, len(servicos_dia) + 1, 2): 
        servicos_dia[j] = int(servicos_dia[j]) #TRANSFORMANDO SERVICOS STR EM INT
    
    compareceram = int(input())
    
    pedidos = []
    for _ in range(compareceram):
        b = input().split()
        pedidos.append(b)

    pedidos_juntos = []
    for lista in pedidos:
        pedidos_juntos += lista


    # DEF NAO DISPONIVEL
    nao_disponivel = []
    
    for i in range(1, len(pedidos_juntos) + 1, 2):
        if pedidos_juntos[i] not in servicos_dia:
            nao_disponivel.append(pedidos_juntos[i - 1])


    # DEF ATENDIDOS/NAO ATENDIDOS
    atendidos = []
    nao_atendidos = []
    
    for i in range(1, len(pedidos_juntos), 2):
        animal = pedidos_juntos[i - 1]
        pedido = pedidos_juntos[i]
        if pedido in servicos_dia:
            quantidade_servicos = servicos_dia[servicos_dia.index(pedido) + 1]
            if quantidade_servicos > 0:
                atendidos.append(animal)
                servicos_dia[servicos_dia.index(pedido) + 1] -= 1
            elif quantidade_servicos == 0:
                nao_atendidos.append(animal)
        
    
        
    #DEFININDO BRIGAS
    brigas_dia = 0
    for k in range(0, len(briguentos), 2):
        if (briguentos[k] in pedidos_juntos) and (briguentos[k + 1] in pedidos_juntos):
            brigas_dia += 1

    # SAIDAS
    print('Dia:', l)
    print('Brigas:', brigas_dia)
    if len(atendidos) != 0:
        print('Animais atendidos: ', end="")
        print(*atendidos, sep = ', ')
    if len(nao_atendidos) != 0:
        print('Animais não atendidos: ', end="")
        print(*nao_atendidos, sep = ', ')
    if len(nao_disponivel) != 0:
        for n in range(len(nao_disponivel)):
            print('Animal', nao_disponivel[n], 'solicitou procedimento não disponível.')
    print()