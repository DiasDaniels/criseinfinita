from time import sleep
import sys
def printWSleep():
    for x in range(9):
        sleep(0.25)
        print('=', end= " ", flush= True)
    print('=')
  
def separador():
    print('||✝'*30)

  
def print1by1(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(delay)
    print
