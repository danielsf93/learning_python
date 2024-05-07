#importando a ferramenta/biblioteca
import pyautogui
#importando o sleep para fazer pausas
import time



#colocando tempo de pause - 0.5 é meio segundo
pyautogui.PAUSE = 1


#automação:
#abrir o menu linux
#You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev
pyautogui.press("win")

#escrever
pyautogui.write("firefox")

#enterhttps?www.google.com.br
pyautogui.press("enter")

pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 'tab')
pyautogui.hotkey('ctrl', 'tab')
pyautogui.hotkey('ctrl', 'w')
pyautogui.hotkey('ctrl', 'w')