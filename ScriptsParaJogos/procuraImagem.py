from pyautogui import locateCenterOnScreen , click

while True: #variavel 'r' recebe uma imagem da pasta do pc
            #e tenta localizar se tem uma imagem igual na tela
            #caso ache uma imagem igual na tela, ela recebe a localização x,y da imagem
            
    r = locateCenterOnScreen('/Users/Samsung/Documents/imagem.png', grayscale=False)
    if r != None:   # caso não ache a imagem, a variavel recebe o valor none
        click(r)
    print (r)