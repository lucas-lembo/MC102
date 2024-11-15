print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.')
print('Seu SO anterior era Linux?\n(0) Não\n(1) Sim')

resposta_a = input()

if resposta_a == '0':
    print('Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim')
    resposta_a_b= input()
    if resposta_a_b == '0':
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.')
    elif resposta_a_b == '1':
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.')
    else:
        print('Opção inválida, recomece o questionário.')

elif resposta_a == '1':
    print('É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas')
    resposta_a_c = input()
    if resposta_a_c == '0':
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.')
    elif resposta_a_c == '1':
        print('Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim')
        resposta_a_c_d = input()
        if resposta_a_c_d == '0':
            print('Já utilizou Arch Linux?\n(0) Não\n(1) Sim')
            resposta_a_c_d_e = input()
            if resposta_a_c_d_e == '0':
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.')
            elif resposta_a_c_d_e == '1':
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.')
            else:
                print('Opção inválida, recomece o questionário.')
        elif resposta_a_c_d == '1':
            print('Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim')
            resposta_a_c_d_f = input()
            if resposta_a_c_d_f == '0':
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.')
            elif resposta_a_c_d_f == '1':
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.')
            else:
                print('Opção inválida, recomece o questionário.')
        else:
            print('Opção inválida, recomece o questionário.')
    elif resposta_a_c == '2':
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.')
    else:
        print('Opção inválida, recomece o questionário.')
else:
    print('Opção inválida, recomece o questionário.')