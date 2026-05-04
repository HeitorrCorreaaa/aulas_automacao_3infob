import pyautogui

box = pyautogui.locateOnScreen('aula6\\btn_8.png')
centro_box = pyautogui.center(box)
print(centro_box)

#opção2

xy2 = pyautogui.locateCenterOnScreen('aula6\\btn_8.png', confidence=0.95)
print(xy2)