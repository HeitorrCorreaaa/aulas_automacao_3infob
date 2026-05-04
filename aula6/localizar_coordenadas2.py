import pyautogui

xy3 = pyautogui.locateCenterOnScreen('aula6\\btn_vermelho.png', confidence=0.90, grayscale=False)

print(xy3)

pyautogui.click(xy3, duration=1)