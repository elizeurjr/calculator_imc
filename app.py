import PySimpleGUI as sg
from tools import calcula_imc,classificar_imc

sg.theme('BlueMono')

layout = [
    [sg.Text('Digite seu nome',size=(12,1)),sg.Input(key='nome',size=(30,1))],
    [sg.Text('Digite seu peso',size=(12,1)),sg.Input(key='peso',size=(30,1))],
    [sg.Text('Digite sua altura',size=(12,1)),sg.Input(key='altura',size=(30,1))],
    [sg.Text(key='resultado',size=(16,1))],
    [sg.Button(button_text='Calcular')]
]

window = sg.Window('Calculadora de IMC',layout=layout)

while True:
    event,values = window.Read()
    peso = int(values['peso'])
    altura = float(values['altura'])

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calcular':
        resultaCalcIMC = round(calcula_imc(peso,altura),2)
        imcClassificado = classificar_imc(resultaCalcIMC)
    if imcClassificado == 'Muito abaixo do peso':
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='white')
    elif imcClassificado == 'Abaixo do peso':
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='white')
    elif imcClassificado == 'Peso normal':
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='SkyBlue1')
    elif imcClassificado == 'Acima do peso':
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='yellow')
    elif imcClassificado == 'Obesidade I': 
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='red')
    elif imcClassificado == 'Obesidade II (severa)': 
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='red')
    elif imcClassificado == 'Obesidade III (mórbida)': 
        window['resultado'].update(imcClassificado)
        window['resultado'].update(background_color='red')