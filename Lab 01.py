Sheila = input() #INTERESTRELAR
Reginaldo = input() #JORNADA NAS ESTRELAS

if Sheila=='pedra' and (Reginaldo=='tesoura' or Reginaldo=='lagarto'):
    print('Interestelar');
elif Sheila=='pedra' and (Reginaldo=='papel' or Reginaldo=='spock'):
    print('Jornada nas Estrelas');
elif Sheila=='pedra' and Reginaldo=='pedra':
    print('empate');
elif Sheila=='papel' and (Reginaldo=='pedra' or Reginaldo=='spock'):
    print('Interestelar');
elif Sheila=='papel' and (Reginaldo=='tesoura' or Reginaldo=='lagarto'):
    print('Jornada nas Estrelas');
elif Sheila=='papel' and Reginaldo=='papel':
    print('empate');
elif Sheila=='tesoura' and (Reginaldo=='papel' or Reginaldo=='lagarto'):
    print('Interestelar');
elif Sheila=='tesoura' and (Reginaldo=='pedra' or Reginaldo=='spock'):
    print('Jornada nas Estrelas');
elif Sheila=='tesoura' and Reginaldo=='tesoura':
    print('empate');
elif Sheila=='lagarto' and (Reginaldo=='papel' or Reginaldo=='spock'):
    print('Interestelar');
elif Sheila=='lagarto' and (Reginaldo=='pedra' or Reginaldo=='tesoura'):
    print('Jornada nas Estrelas');
elif Sheila=='lagarto' and Reginaldo=='lagarto':
    print('empate');
elif Sheila=='spock' and (Reginaldo=='tesoura' or Reginaldo=='pedra'):
    print('Interestelar');
elif Sheila=='spock' and (Reginaldo=='lagarto' or Reginaldo=='papel'):
    print('Jornada nas Estrelas');
elif Sheila=='spock' and Reginaldo=='spock':
    print('empate');