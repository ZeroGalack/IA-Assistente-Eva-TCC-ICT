import serial
#import time
import cv2
import re
import webbrowser
from gtts import gTTS
from pygame import mixer
import os
#from datetime import date
#import threading

cap = cv2.VideoCapture(0)

try:
    PortaSerial = serial.Serial.close
    PortaSerial = serial.Serial('COM8', 9600)
    print('arduino ok')

except serial.serialutil.SerialException:
    print('arduino n ok')


def arduino(codigo, printarVl=True):
    try:
        cod = str(codigo) + '#'
        if printarVl:
            print(codigo)
        PortaSerial.write(cod.encode())#

    except AttributeError:
        if printarVl:
            print('arduino não conectado')
        else:
            pass


def comparar(palavras, fala):
    for palavras in palavras:
        if palavras in fala.split():
            return True


def pesquise(text):
    procura = re.sub(r'eva|pesquisa|pesquise|pesquisar|procure|procurar|por|na|internet', '', text)
    url = "https://www.google.co.in/search?q=" + (procura) + "&oq=" + (procura
    ) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.open_new(url)
    print('pesquisando ' + procura)
    engine_say('pesquisando ' + procura)


def engine_say(text):
    try:
        tts = gTTS(text=text, lang="pt-br")
        tts.save("audios/engine_say.mp3")
        mixer.init()
        mixer.music.load("audios/engine_say.mp3")
        mixer.music.play()
    except:
        mixer.init()
        mixer.music.load("audios/sem_internet.mp3")
        mixer.music.play()
    while mixer.music.get_busy():  # check if the file is playing
        pass
    mixer.music.load("audios/engine_say_copy.mp3")
    os.remove("audios/engine_say.mp3")

'''def Sensor_Monitoring():
    while True:
        try:
            msg = PortaSerial.readline()
            msg = str(msg)
            msg = msg[(msg.index('<')
                    +1):msg.index('>')]
            msg = msg.split(',')

            S1 = int(msg[0])
            S2 = int(msg[1])

            if S1 < 200:
                arduino(4, False)
            if S1 > 200:
                arduino(-4, False)
        except AttributeError:
            pass'''


def reprodutor_audio(audio_a_tocar):
        mixer.init()
        mixer.music.load(audio_a_tocar)
        mixer.music.play()




'''def date_time(data=False, hora=False, day_week=False):
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
            if date_time(hora=True) == '06:00:00':
                print(date_time(hora=True))
                thread = threading.Thread(target=reprodutor_audio, args=['audios/--hino-do-flamengo-2019-funk.mp3'])
                thread.start()
                time.sleep(1)
'''
