import serial
import re
import webbrowser
from gtts import gTTS
from pygame import mixer
import os
import threading

COM = str(input('Digite a Porta COM: '))
try:
    PortaSerial = serial.Serial.close
    PortaSerial = serial.Serial(COM, 9600)
    print('Arduino conectado')

except serial.serialutil.SerialException:
    print('Arduino não conectado')


def arduino(codigo, printarVl=True):
    try:
        cod = str(codigo) + '#'
        if printarVl:
            print(codigo)
        PortaSerial.write(cod.encode())#

    except AttributeError:
        if printarVl:
            print('Arduino não conectado')
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
    threading.Thread(target=engine_say, args=['pesquisando ' + procura]).start()


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


def reprodutor_audio(audio_a_tocar):
        mixer.init()
        mixer.music.load(audio_a_tocar)
        mixer.music.play()
