jogadores = []
total = []
dados = {}
gol = []

while True:
    dados['nome'] = input('Nome do Jogador: ').capitalize()
    total = int(input(f'Total de jogos do {dados["nome"]}: '))
    for c in range(0, total):
        gol.append(int(input(f'Quantos gols {dados["nome"]} marcou na {c} partida? ')))
    dados['gols'] = gol.copy()
    gol.clear()
    jogadores.append(dados.copy())
    dados.clear()
    resp = input('Continuar? ').upper()
    if resp == 'N':
        break
print()
while True:
    opc = int(input('Você quer saber os dados de qual jogador? '))
    if opc == 999:
        break
    if opc < len(jogadores):
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}')
        print('-' * 16)
        print(jogadores[opc])
        for i, v in enumerate(jogadores[opc]['gols']):
            print(f'Na {i} partida marcou {v}')
    else:
        print('Opção inválida.')
