from keyboard import is_pressed , write , press

def macro1(): 
    write("exemplo1")
    press('enter')

def macro2():
    write("exemplo2")
    press('enter')

def macro3():
    write("exemplo3")
    press('enter')

while True: #macro: quando pressionarem as teclas f7 ou f8 ou f9 escreva algo
    if is_pressed('f7'):
        macro1()
    elif is_pressed('f8'):
        macro2()
    elif is_pressed('f9'):
        macro3()
