import os
perg = input('''A pasta já esta clonada? 
[s]sim ou [n]não
:''').lower()
if perg == 'n':
    os.system('git clone https://github.com/oleoz1n/Fiap')
    print('Coloca o push.py dentro dela e abre de novo')
else:
    arquivo = input('Qual o nome do arquivo?: ')
    os.system('git init')
    os.system(f'git add {arquivo}')
    os.system(f'git commit -m \"adicionando {arquivo}\"')
    os.system('git remote add origin https://github.com/oleoz1n/Fiap.git')
    os.system('git branch -M main')
    os.system('git push -u origin main')