import random
import time


def collatz(x):
    if (x % 2 == 0):
        return x/2
    else:
        return 3 * x + 1

green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
white = '\033[37m'

while(1 == 1):
    delay = 0.33

    print('input a number')
    olle = input('Type "0" to exit')
    if (olle == '0'):
        break
    
    steps = 1
    pelle = collatz (int (olle))
    while (pelle>1):

        # Random color
        gurka = random.randint(1, 5)
        if(pelle % 2 == 1):
            print (red)
        else:
            print(green)

        print (int (pelle))
        pelle = collatz(pelle)
        steps = steps + 1
        time.sleep(delay)
        if (steps % 10 == 0):
            delay = delay * 0.8

    print (int (pelle))
    print(yellow)
    print ('No of steps: ' + str(int (steps)))
    print (white)
