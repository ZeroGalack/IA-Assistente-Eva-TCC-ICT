from time import time

tpin = 0
globals()['tpin'] = int(time())

while True:
    tp = int(time())
    print(tp - tpin)

    if tp - tpin == 6:
        print('foifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoifoi')
        globals()['tpin'] = tp