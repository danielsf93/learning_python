#anterior:
#python3 --version
#pip install pyautogui
#sudo apt install python3-pip
#pip install pyautogui
#pip install pandas

#importando a ferramenta/biblioteca
import pyautogui
#importando o sleep para fazer pausas
import time



#colocando tempo de pause - 0.5 é meio segundo
pyautogui.PAUSE = 0.5


#automação:
#abrir o menu linux
#You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev
pyautogui.press("win")

#escrever
pyautogui.write("firefox")

#enterhttps?www.google.com.br
pyautogui.press("enter")

#escrever
#problemas com caracter / em linux
#caracteres resolvidos com "setxkbmap br" no terminal
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#dar uma pausa para o site carregar
time.sleep(2)

#clicar na posição de login
#para encontrar as posições de mouse, criar auxiliar.py 
#click esquerdo
pyautogui.click(x=543, y=308)
#escrever email
pyautogui.write("danielsilva@usp.br")

#tab
pyautogui.press("tab")
pyautogui.write("12345678")
#executa login
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)
#pip install pandas numpy openpyxl


#importar base de dados .csv
import pandas as pd

#variavel com informações da tabela
tabela = pd.read_csv("produtos.csv")


#foreach loop

for linha in tabela.index:


    #clicar em código do produto
    pyautogui.click(x=650, y=238)
    #variavel de codigo da tabela
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #Marca do Produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    #Tipo do Produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    #Categoria do Produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    #Preço Unitário do Produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    #Custo do Produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    #OBS
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter")

    #subir a página
    pyautogui.scroll(5000)



