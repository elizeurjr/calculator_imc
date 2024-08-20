def calcula_imc(peso,altura):
    resultadoimc = peso / (altura * altura)
    return resultadoimc

def classificar_imc(resultaCalcIMC):
        # abaixo de 17 = Muito abaixo do peso
        if resultaCalcIMC < 17:
           # print('Muito abaixo do peso')
            return'Muito abaixo do peso'
        # entre 17 e 18.5 = Abaixo do peso
        elif 17 <= resultaCalcIMC < 18.5:
           # print('Abaixo do peso')
            return 'Abaixo do peso'
        # entre 18.5 e 24.9 = Peso normal
        elif 18.5 <= resultaCalcIMC < 25:
           # print('Peso normal')
            return 'Peso normal'
        # entre 25 e 29.9 = Acima do peso
        elif 25 <= resultaCalcIMC < 30:
           # print('Acima do peso')
            return 'Acima do peso'
        # entre 30 e 34.9 = Obesidade I
        elif 30 <= resultaCalcIMC < 35:
           # print('Obesidade I')
            return 'Obesidade I'
        # entre 35 e 39.9 = Obesidade II (severa)
        elif 35 <= resultaCalcIMC < 40:
           # print('Obesidade II (severa)')
            return 'Obesidade II (severa)'
        # acima de 40 = Obesidade III (mórbida)
        elif resultaCalcIMC >= 40:
           # print('Obesidade III (mórbida)')
            return 'Obesidade III (mórbida)'