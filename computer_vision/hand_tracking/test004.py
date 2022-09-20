import requests

while True:
    r = requests.get('https://test7.lucasteixeira23.repl.co/garraTeste')
    r = str(r.json())
    if r != '':
        print(r)