print('Iniciando...')

import requests
from computer_vision.hand_tracking.volume_controll import volume_controller, varHVC
from computer_vision.hand_tracking.hand_sinais import hand_sinais, varHS
from computer_vision.face_rec.face_indentification import FaceIndetification
from functions import *
import threading
from GPT_3 import *
LH = ''

print("""
EEEEEEEEEEEE  VVV              VVV     AAA              
EEE            VVV            VVV     AAAAA      
EEE             VVV          VVV     AAA AAA            
EEE              VVV        VVV     AAA   AAA        
EEEEEEEEEEEE      VVV      VVV     AAA     AAA     
EEE                VVV    VVV     AAAAAAAAAAAAA     
EEE                 VVV  VVV     AAA         AAA     
EEE                  VVV VV     AAA           AAA   
EEEEEEEEEEEE          VVVV     AAA             AAA       
""")


def main(HomeSet):

    if HomeSet == "LucasCordeiro":
        globals()['LH'] = '77'
        print('Bem vindo Lucas Cordeiro')

    if HomeSet == "LucasFernandes":
        globals()['LH'] = '44'
        print('Bem vindo Lucas Fernades')

    if HomeSet == "Thais":
        globals()['LH'] = '55'
        print('Bem vinda Thais')

    if HomeSet == "William":
        globals()['LH'] = '22'
        print('Bem vindo William')

    if HomeSet == "Miguel":
        globals()['LH'] = '33'
        print('Bem vindo Miguel')

    if HomeSet == "desconhecido":
        globals()['LH'] = '11'
        print('Bem vindo desconhecido')

    arduino(LH)

    while True:
        try:
            r = requests.get('https://test7.lucasteixeira23.repl.co/r')
            fala = str(r.json())
            fala = fala.lower()
            n = 0

            if fala != "" and comparar(['eva'], fala):
                print(fala)

                if comparar(['ligar', 'ligue', 'liga', 'acenda', 'acender'], fala):
                    if comparar(['luz', 'lampada', 'lmpada', 'luzes'], fala):
                        n += 1
                        threading.Thread(target=engine_say, args=['Ligando luz']).start()
                        threading.Thread(target=arduino(codigo=[LH])).start()

                    if comparar(['maozinha'], fala):
                        if comparar(['volume'], fala):
                            n += 1
                            threading.Thread(target=engine_say, args=['Ligando mãozinha volume']).start()
                            threading.Thread(target=varHVC, args=['start']).start()
                            threading.Thread(target=volume_controller).start()

                        if comparar(['sinais'], fala):
                            n += 1
                            threading.Thread(target=engine_say, args=['Ligando mãozinha Sinais']).start()
                            threading.Thread(target=varHS, args=['start']).start()
                            threading.Thread(target=hand_sinais).start()

                if comparar(['desligar', 'desligue', 'desliga', 'apague', 'apagar'], fala):
                    if comparar(['luz', 'lampada', 'lmpada', 'luzes'], fala):
                        n += 1
                        threading.Thread(target=engine_say, args=['Desligando luz']).start()
                        threading.Thread(target=arduino, args=['-1']).start()

                    if comparar(['maozinha'], fala):
                        if comparar(['volume'], fala):
                            n += 1
                            print('Desligando Hand Tracking')
                            threading.Thread(target=engine_say, args=['Desligando mãozinha volume']).start()
                            threading.Thread(target=varHVC, args=['stop']).start()

                        if comparar(['sinais'], fala):
                            n += 1
                            print('Desligando Hand Tracking')
                            threading.Thread(target=engine_say, args=['Desligando mãozinha Sinais']).start()
                            threading.Thread(target=varHS, args=['stop']).start()

                    if comparar(['musica'], fala):
                        n += 1
                        mixer.music.stop()

                if comparar(['pesquisa', 'pesquise', 'pesquisar', 'procure', 'procurar'], fala) and comparar(['internet'], fala):
                    n += 1
                    threading.Thread(target=engine_say, args=['Pesquisando na Internet']).start()
                    threading.Thread(target=pesquise, args=[fala]).start()

                if comparar(['tocar', 'toque'], fala):
                    n += 1
                    NameMusica = re.sub(r'eva|toque|tocar|musica', '', fala)
                    NameMusica = re.sub(' ', '-', NameMusica)
                    threading.Thread(target=reprodutor_audio, args=[f'audios/{NameMusica}.mp3']).start()

                if comparar(['musica'], fala):
                    if comparar(['pausar'], fala):
                        n += 1
                        mixer.music.pause()

                    if comparar(['despausar'], fala):
                        n += 1
                        mixer.music.unpause()

                if comparar(['pare', 'para'], fala) and comparar(['falar'], fala):
                    n += 1
                    engine_say('Ok')
                    mixer.music.stop()

                if n == 0:
                    threading.Thread(target=GPT3, args=[fala]).start()

        except requests.exceptions.SSLError:
            print(f'ERRO1')

        except requests.exceptions.ConnectionError:
            print(f'ERRO2')

        except requests.exceptions:
            print(f'ERRO3')

        except TypeError:
            print(f'ERROR4')


def run_main():
    for n in range(5):
        senha = str(input('Digite sua Senha: '))
        if senha == '22558800':
            name = FaceIndetification()

            if name == 'Lucas Cordeiro':
                engine_say('Bem vindo, Lucas Cordeiro')
                threading.Thread(target=reprodutor_audio, args=['audios/--feeling-good.mp3']).start()
                main("LucasCordeiro")

            if name == 'Thais':
                engine_say('Bem vinda, Thaís')
                threading.Thread(target=reprodutor_audio, args=['audios/--todas-as-estrelas.mp3']).start()
                main("Thais")

            if name == 'William':
                engine_say('Bem vindo, William')
                threading.Thread(target=reprodutor_audio, args=['audios/--boa-menina.mp3']).start()
                main("William")

            if name == 'Lucas Fernandes':
                engine_say('Bem vindo, Lucas Fernades')
                threading.Thread(target=reprodutor_audio, args=['audios/--hino-do-vasco-da-gama.mp3']).start()
                main("LucasFernandes")

            if name == 'Miguel':
                engine_say('Bem vindo, Miguel')
                threading.Thread(target=reprodutor_audio, args=['audios/--nightfall-remastered-2007.mp3']).start()
                main("Miguel")

            if name == 'Unknown':
                engine_say('Bem vindo, desconhecido')
                threading.Thread(target=reprodutor_audio, args=['audios/--musica-de-elevador.mp3']).start()
                main("desconhecido")
        else:
            print('senha incorreta')