# COMEÇO DA DEFINIÇÃO DE QUANTIDADE#
def VolumefeijoadaML ():
    while True:
        try:
            print('Volume de feijoada')
            VolumeF = float(input('Volume de feijao de 300 ml a 5000ml: '))
            if 300<= VolumeF <=5000 :
                return VolumeF*0.08
            else:
                print('Não trabalhamos com porções menores de 300 mls e acima de 5L')
                continue
        except ValueError:
            print('Digite apenas numeros')
            continue
 # FIM DA DEFINIÇÃO DE QUANTIDADE#
#COMEÇO DEFINIÇÃO DE TIPO DE FIJOADA#
def Tipodefeijoada ():
    while True:
        print('Opção de feijoada basica(feijao+paiol+ costelinha)')
        print('premium( feijao+ paiol+  costelinha+ partes de porco)')
        print('suprema(feijao+ paiol+  costelinha+ partes de porco+ charque+ calabresa+ bacon)')
        TipoF = input('defina a feijoada escolhida: b=basica, p=premium e s=suprema')
        if TipoF=='b':
            return 1.00
        elif TipoF== 'p':
            return 1.25
        elif TipoF== 's':
            return 1.50
        else:
            print('Pare de digitar funções inexistentes')
            continue
# FIM DA DEFINIÇÃO DE TIPO DE FEIJOADA#
# COMEÇO DA DEFINIÇÃO DE ACOMPANHAMENTOS#
def Acompanhamentos():
    Acomp = 0
    while True:
        print('Deseja acompanhamento:')
        print('0- Sem mais acompanhamentos(Encerrar)')
        print('1- 200g de arroz')
        print('2- 150g de farofa especial')
        print('3- 100g de couve cozida')
        print('4- 1 laranja descascada')
        Acompa= int(input('acompanhamento de 0 a 4'))
        if Acompa== 1:
            Acomp= Acomp+5
        elif Acompa== 2:
            Acomp=Acomp+6
        elif Acompa== 3:
           Acomp= Acomp+7
        elif Acompa== 4:
            Acomp=Acomp+3
        elif Acompa== 0:
            return Acomp
        else:
            print('digite uma opção válida')
# FIM DA DEFINIÇÃO DE ACOMPANHAMENTOS#
# COMEÇO DA MAIN#
print('Bem vindo ao programa de feijoada do Guilherme Klein Klug')
while True:
    vfeijoada= VolumefeijoadaML()
    tipo=Tipodefeijoada()
    Acompanhamento= Acompanhamentos()
    print('{:.2f}'.format(vfeijoada))
    print('{:.2f}'.format(tipo))
    print('{:.2f}'.format(Acompanhamento))
    Total= vfeijoada*tipo+Acompanhamento
    print('Valor total foi de R$ {:.2f} '.format(Total))
#FIM DA MAIN#
