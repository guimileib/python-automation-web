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

# 3. Importar base de dados
tabela = pandas.read_csv("produtos.csv") # Tabela recebe 

print(tabela)

# 4. Cadastrar 1 produto
'''codigo = 'MOLO000251'
marca = 'Logitech'
tipo = 'Mouse'
categoria = "1"
preco_unitario = "25.95"
custo = "6.5"
obs = '''

#  Estava dando bug
for linha in tabela.index:
    pyautogui.click(x=802, y=279) # Entrar no primeiro campo   

    codigo = tabela.loc[linha, "codigo"] # .loc[linha, coluna]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = tabela.loc[linha, "categoria"]    
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = tabela.loc[linha, "obs"]
    if obs != 'nan':
        pyautogui.write(str(obs))
        
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000) # A cada 100 é um pixel de scroll
