n_jogadores = int(input())
num_caixa_1 = (input()).split()
num_caixa_2 = (input()).split()
pontuacao = []
p = 0

# Numero de Jogadores Par ou Impar
if n_jogadores % 2 == 0:
    margem = 0
else:
    margem = 1

# Calculos
for i in range(1, n_jogadores // 2 + margem + 1):
    pontuacao.append((int(num_caixa_2[p + 1]) - int(num_caixa_2[p])) * int(num_caixa_1[i - 1]))
    p += 2


for i in range(n_jogadores // 2 + margem + 1, n_jogadores + 1):
    pontuacao.append((int(num_caixa_2[p + 1]) - int(num_caixa_2[p]) + int(num_caixa_1[i - 1])))
    p += 2

# Definicao do Resultado
n_maximo = 0
empate = []
vencedor = 0

for i in range(len(pontuacao)):
    if pontuacao[i] >= n_maximo:
        n_maximo = pontuacao[i]
        vencedor = i
   
for i in range(len(pontuacao)):
    if pontuacao[i] == n_maximo:
        empate.append(n_maximo)

# Impressao do Resultado
if len(empate) != 1:
    print('Rodada de cerveja para todos os jogadores!')
else:
    print('O jogador número', vencedor + 1, 'vai receber o melhor bolo da cidade pois venceu com', n_maximo, 'ponto(s)!')