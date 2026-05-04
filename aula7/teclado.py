import pyautogui
import time

#abre uma janela de entrada de dados
pergunta = pyautogui.prompt('o que deseja saber hoje')

#pressiona um atalho do teclado
#(win + d minimiza janelas e mostra desktop)
pyautogui.hotkey ("win", "d")

#pressiona a tecla win
pyautogui.press('win')

#digita um texto da onde o curso está
pyautogui.write('chrome')

#pressiona a tecla enter
pyautogui.press('enter')

#faz uma pausa de 2 segundos
time.sleep(2)

#digita um endereço na url
pyautogui.write("https://www.chatgpt.com")
pyautogui.press("enter")

#faz uma pausa
time.sleep(3)

#digita o texto armazenado na variavel pergunta
pyautogui.write(pergunta)
pyautogui.press('enter')

#faz uma pausa
time.sleep(6)

while True:
    time.sleep(2)
    try:
#localiza a coordenada da seta
        xy = pyautogui.locateCenterOnScreen('aula7\\seta.png', confidence = 0.8)
        pyautogui.click(xy)
        break
    except:
        print("ainda processando...")

time.sleep(3)
#localiza a coordenada do copiar
xy2 = pyautogui.locateCenterOnScreen('aula7\\copiar.png', confidence =.98)

pyautogui.click(xy2)


#faz uma pausa
time.sleep(2)

#abre outra guia no chrome
pyautogui.hotkey('ctrl', 't')

#faz uma pausa
time.sleep(1)

#digita o endereço
pyautogui.write('https://www.gmail.com')
pyautogui.press('enter')

time.sleep(3)

xy3 = pyautogui.locateCenterOnScreen('aula7\\escrever_gmail.png', confidence =0.95)
pyautogui.click(xy3)

time.sleep(3)

pyautogui.write("softip@gmail.com")
pyautogui.press('tab')
pyautogui.write('pesquisa automatizada')
pyautogui.press("tab")
pyautogui.hotkey('ctrl', 'v')

xy4 = pyautogui.locateCenterOnScreen('aula7\\enviar.png', confidence =0.95)

pyautogui.click(xy4)

