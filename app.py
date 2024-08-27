#Crie um programa para automatizar o envio de um programa qualquer para o repositório remoto do GitHub.
# Ao terminar, gere o executável e envie o código-fonte e a pasta do executável.

#importar bibliotecas
import pyautogui as auto

auto.PAUSE = 0.5

#maximizar a tela, a janela do chrome
auto.hotkey('ctrl', 'j')

#abrir o git init
# auto.write('git init')
#auto.press('enter') #aperta enter

# auto.write('git status')
#auto.press('enter') #aperta enter

# auto.write(''git add .)
#auto.press('enter') #aperta enter

#echo .venv > .gitignore
#auto.press('enter') #aperta enter

#git commit -m "Automatizar comando github"
#auto.press('enter') #aperta enter

#git branch -M main
#auto.press('enter') #aperta enter

#git remote add origin https://github.com/JenniferMelissa/repositorio_github.git
#auto.press('enter') #aperta enter

#git push -u origin main
#auto.press('enter') #aperta enter

