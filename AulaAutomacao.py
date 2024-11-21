import pyautogui 
import time

#Parar não perder o controle da automação
pyautogui.FAILSAFE = True

#Pausa de 0.3 segundos (300 milisegundos)
'''pyautogui.PAUSE = 0.3


#Espera um tempo para rodar
time.sleep(5)

pyautogui.click (x=1801, y=16)

pyautogui.click (x=600, y=1056)
#Pegar posição do mouse 
#print(pyautogui.position())

#Pegar o tamanho da tela/resolução.
#print(pyautogui.size())

#Clicar com o mouse
pyautogui.click(x=405, y=303)

#Clicar com o botão direito do mouse
#pyautogui.click(x=395, y=375, button="right")

#Dois cliques no mouse
#pyautogui.click(x=395, y=375, click="2")

#Mover o mouse
pyautogui.moveTo(x=696, y=176, duration=1)

pyautogui.click(x=1182, y=266)

time.sleep(3)

pyautogui.scroll(-2000)

pyautogui.click(x=1059, y=472)

pyautogui.click(x=491, y=334)'''

#Funções do teclado 
pyautogui.press("win")

#Para escrever
pyautogui.write("Clima", interval=0.25)

pyautogui.press("enter")

#Para pressionar duas teclas 
#pyautogui.hotkey("ctrl", "v")