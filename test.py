'''import time

lista = {}

def add_timers():
    for i in range(3):
        desc = ''
        nome = input('diga um nome para o timer: ')

        if input('add descrição? sim/nao: ') == 'sim':
            desc = input('diga uma descrição para o timer: ')
        else:
            desc = None

        tp = input('diga um tp para o timer: ')
        print(f'{nome}/{desc}/{tp}')

        lista[nome] = f'{desc}/{tp}'

        print(lista)


def timers():
    tp = time.localtime()
    tp = time.strftime('%d/%m/%Y %H:%M', tp)
    print(tp)


add_timers()
print(lista)'''
import time

'''vdd = float(input('vdd ='))
rd = float(input('rd = '))
idss = float(input('idss = '))
vgsoff = float(input('vgsoff ='))
vgs = float(input('vgs = '))
rg = float(input('rg = '))

id = idss*(1-(vgs/vgsoff))**2
print(f'ID= {id}')

vds = vdd - rd*id
print(f'vds= {vds}')

vd = vds
print(f'VD= {vd}')'''

import re
text = """
# Quanto maior o prompt maior vai ser o gasto de tokens
def GPT3(fala):
prompt = "
Human: Qual é o seu nome?
AI: O meu nome é Eva.

Human: Por quem você foi desenvolvida?
AI: Por Cordeiro, Fernandes, Thaís, William e Miguel."

print('...')
while True:
print(f'Human: {fala}')

prompt += fala
# prompt = trans.translate(prompt, dest='en').text
answer, prompt = gpt3(prompt,
temperature=0.9,
frequency_penalty=0,
presence_penalty=0.8,
top_p=1,
start_text='\nAI:',
restart_text='\nHuman: ')
# stop_seq=['\nHuman:', '\n']
resposta = trans.translate(answer, dest='pt').text
print('IA: ' + resposta)
engine_say(resposta)
return resposta    

text = re.sub(r'\n|TESTTESTTEST', ' ', text)
print("Explique essa função em Python: "+text)

import serial

try:
    PortaSerial = serial.Serial.close
    PortaSerial = serial.Serial('COM8', 9600)
    print('arduino ok')

except serial.serialutil.SerialException:
    print('arduino n ok')

while True:
    msg = PortaSerial.readline()
    msg = msg
    print(msg)

    arquivo = open('arq02.txt', 'a')
    arquivo.write(f"{msg}")
    time.sleep(1)
"""
'''import time
from datetime import date
import threading

def date_time(data=False, hora=False, day_week=False):
    dias_da_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    tp = time.localtime()
    dia_da_semana = time.strftime('%d/%m/%Y', tp).split('/')
    dia_da_semana = dias_da_semana[date(int(dia_da_semana[-1]), int(dia_da_semana[-2]), int(dia_da_semana[-3])).weekday()]
    if day_week:
        #print(dia_da_semana)
        return dia_da_semana

    data_hora = time.strftime('%d/%m/%Y-%H:%M:%S', tp).split('-')
    if data:
        #print(data_hora[0])
        return data_hora[0]
    if hora:
        #print(data_hora[1])
        return data_hora[1]

def timers():
    while True:
        if date_time(day_week=True) == 'segunda' or 'terça' or 'quarta' or 'quinta' or 'sexta':
            if date_time(hora=True) == '20:46:40':
                print(date_time(hora=True))
                print("O GLORIA")
                time.sleep(1)


thread = threading.Thread(target=timers)
thread.start()'''
import re

NameMusica = 'eva toque todas as estrelas'
print(NameMusica)
NameMusica = re.sub(r'eva|toque|tocar|musica', '\r', NameMusica)
NameMusica = re.sub(' ', '-', NameMusica)
print(NameMusica)