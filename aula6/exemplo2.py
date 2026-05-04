import pyautogui

xy8 = pyautogui.locateCenterOnScreen ('aula6\\btn_8.png', confidence = 0.95)
pyautogui.click(xy8, duration=1)

xy_mais = pyautogui.locateCenterOnScreen ('aula6\\btn_+.png', confidence = 0.95)
pyautogui.click(xy_mais, duration=1)

xy2 = pyautogui.locateCenterOnScreen ('aula6\\btn_2.png', confidence = 0.95)
pyautogui.click(xy2, duration=1)

xy_igual = pyautogui.locateCenterOnScreen ('aula6\\btn_=.png', confidence = 0.95)
pyautogui.click(xy_igual, duration=1)

