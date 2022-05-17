import pyautogui
#primer pregunta
pyautogui.click(x=369, y=411, clicks=1)
pyautogui.press('tab')
pyautogui.press('tab')
#segunda pregunta
pyautogui.write("Al mal tiempo, buena cara", interval=0.25)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
#3 pregunta
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
#4 pregunta 
pyautogui.typewrite("arely")
pyautogui.hotkey('ctrl','alt','q')
pyautogui.typewrite("gmail.com")
pyautogui.press('tab')
pyautogui.press('enter')
#capturar pantalla
screenshot = pyautogui.screenshot()
#guardar imagen
screenshot.save("screenshot.png")

#repetir proceso
pyautogui.click(x=402, y=418, clicks=2, interval=0.50)
#primer pregunta
pyautogui.click(x=369, y=483, clicks=1)
pyautogui.press('tab')
pyautogui.press('tab')
#segunda pregunta
pyautogui.write("A donde el corazon se inclina, el pie camina", interval=0.25)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
#3 pregunta
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
#4 pregunta
pyautogui.typewrite("sarahi")
pyautogui.hotkey('ctrl','alt','q')
pyautogui.typewrite("gmail.com")
pyautogui.press('tab')
pyautogui.press('enter')
#capturar pantalla
screenshot = pyautogui.screenshot()
#guardar imagen
screenshot.save("screenshot1.png")
