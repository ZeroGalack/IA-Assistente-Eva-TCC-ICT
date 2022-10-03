import qrcode

img = qrcode.make('https://drive.google.com/file/d/1j9vHNx0eAisS7w_DE2DtbKWEObw5_pWY/view?usp=sharing')
img.save('QRCode1.png')
print("ok")