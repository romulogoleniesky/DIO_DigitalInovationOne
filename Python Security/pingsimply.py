# Curso de Python Security  - Digital Innovation One
# Instrutor Bruno Dias.
# Aula de Ping Simples

import os

print("\033[1:33:45m#\033[m"*50)
print('\033[1:33:45mDigite um site à ser verificado: \033[m')
print("\033[1:33:45m#\033[m"*50)
site = input('>>>')
os.system(f'ping -n 6 {site}')

