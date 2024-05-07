import pyautogui
import time

# Colocando tempo de pausa global para PyAutoGui
pyautogui.PAUSE = 1

# Pausa para o site carregar antes de iniciar o loop
time.sleep(2)

# Loop infinito
while True:
    try:
        # Clique no primeiro botão usando uma imagem
        x, y = pyautogui.center(pyautogui.locateOnScreen('botao01.png', confidence=0.9))
        pyautogui.click(x, y)

        # Clique no segundo botão usando uma imagem
        x, y = pyautogui.center(pyautogui.locateOnScreen('botao02.png', confidence=0.9))
        pyautogui.click(x, y)

        # Clique no terceiro botão usando uma imagem
        x, y = pyautogui.center(pyautogui.locateOnScreen('botao03.png', confidence=0.9))
        pyautogui.click(x, y)

        # Pausa para garantir que ações anteriores sejam concluídas
        time.sleep(5.5)

        # Usando teclas de atalho
        pyautogui.hotkey('ctrl', 'w')  # Fecha uma aba
        pyautogui.hotkey('tab')  # Alterna para o próximo elemento
        pyautogui.hotkey('ctrl', 'enter')  # Ação com Ctrl+Enter

        # Pequena pausa para evitar sobrecarga
        time.sleep(2)

        # Alternar entre abas
        pyautogui.hotkey('ctrl', 'tab')

        # Adicione uma pausa entre iterações para evitar excessos
        time.sleep(1)
    
    except Exception as e:
        print("Erro encontrado:", e)  # Exibe mensagem de erro
        break  # Interrompe o loop para evitar comportamentos inesperados





