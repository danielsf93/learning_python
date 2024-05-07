#importando a ferramenta/biblioteca
import pyautogui
#importando o sleep para fazer pausas   

import time

#comando que mostra posição do mouse
#time.sleep(5)
#print(pyautogui.position())

#(x=427, y=393)
#(x=410, y=277)

#print(pyautogui.KEYBOARD_KEYS)

# Localize um elemento na tela usando uma imagem e clique nele
# Substitua 'botao.png' pelo nome correto da imagem de referência
location = pyautogui.locateOnScreen('botao.png', confidence=0.9)

if location:
    x, y = pyautogui.center(location)  # Obtém o centro da área encontrada
    pyautogui.click(x, y)  # Clique no centro
else:
    print("Elemento não encontrado!")  # Informe se a imagem não foi encontrada
