import pyautogui
import time 
import pandas
'''
pyautogui.click -> clica em algum lugar
pyautogui.press -> aperta 1 tecla
pyautogui.write -> escrever um texto
pyautogui.hotkey -> combinação de teclas
pyautogui.position -> diz onde esta o seu mouse 
'''

pyautogui.PAUSE = 0.5 # Setando um segundo para cada execucao

# 1. Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o opera
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

# Entrar no site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3) # Setando tempo para esperar fazer uma acao

# 2. Fazer Login

pyautogui.click(x=779, y=389) # Clica no campo de email
pyautogui.write("teste@gmail.com") # Digita
pyautogui.press('tab') 

pyautogui.click(x=720, y=488) # Clica no campo de senha
pyautogui.write('123456') # Digita 
pyautogui.press('enter')

time.sleep(3)


