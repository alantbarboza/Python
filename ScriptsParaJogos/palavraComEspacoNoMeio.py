import pyautogui
from pynput.keyboard import Key, Listener

def on_press(key): #quando pressionar alguma tecla 
    if key != Key.space and key != Key.backspace:  #quando a tecla for diferente de espaço e a tecla apagar
        pyautogui.typewrite(" ") #escreva

def on_release(key): #quando soltar alguma tecla
    print('{0} release'.format(
     key))  #escreva no console qual tecla foi solta
    #if key == Key.esc:      # Stop listener
        #return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

