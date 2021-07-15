from keyboard import is_pressed , write , press
from time import sleep
veref = False
contador = 0
centopeia = ["..╚═(███)═╝", "╚═(███)═╝" , ".╚═(███)═╝" , "..╚═(███)═╝" ,
"…╚═(███)═╝" , "…╚═(███)═╝" , "..╚═(███)═╝"]
while True:
    if is_pressed('f9') and veref == False: #aperte f9 para ativar
        print('on')
        write("Licença. Centopeia passando…")
        press('enter')
        write("……..\…../")
        press('enter')
        write("……╚⊙ ⊙╝")
        press('enter')
        veref = True
        sleep(2)
    elif is_pressed('f9') and veref == True: #aperte f9 denovo por 2s para parar
        veref = False   
        print('stop')
        sleep(2)
    elif veref == True: 
        if contador > 6: #contador serve para mostrar os 7 pedaços do corpo da centopeia
            contador = 0
        write("" + centopeia[contador])
        press('enter')
        sleep(2)
        contador+=1
        