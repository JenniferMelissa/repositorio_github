#Crie um programa para automatizar o envio de um programa qualquer para o repositório remoto do GitHub.
# Ao terminar, gere o executável e envie o código-fonte e a pasta do executável.

#importar bibliotecas
import pyautogui as auto

import time

# tempo que cada comando demora para executar
auto.PAUSE = 1

#pede o link do deiretório
diretorio = input('Informe o link do diretório: ')

# instruções
auto.press('win') #clica na tecla win
auto.write('vscode') #escreve vscode
auto.press('enter') #aperta enter

# espera 10 segundos
time.sleep(10)


auto.hotkey('ctrl', 'shift', "'") #atalho
time.sleep(10) #espera 10 segundos
auto.write('git init') #iniciar repositorio git
auto.press('enter') #aperta enter
auto.write('git add .')  #salvar informacoes do repositorio
auto.press('enter') #aperta enter
auto.write('git commit -m "Automatizar repositório git."')
auto.press('enter') #aperta enter

# espera 5 segundos
time.sleep(5) 

auto.write('git branch -M main') #mudar nome da branch master para mais
auto.press('enter') #aperta enter

auto.write(f'git remote add origin {diretorio}') #adiciona o link do repositorio 
auto.press('enter') #aperta enter 

auto.write('git push -u origin main') #sobe para o repositorio remoto
auto.press('enter') #aperta enter 