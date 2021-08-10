# PING MULTIPLO:
# passo a passo
import os
""" primeiro passo

with open("hosts.txt") as file:
    dump = file.read()
    print(dump)"""

""" segundo passo

with open("hosts.txt") as file:
    dump = file.read().splitlines()
    for ip in dump:
        print(ip)  """
""" terceiro e ultimo passo:"""

with open("hosts.txt") as file:
    dump = file.read().splitlines()
    for ip in dump:
        os.system('ping '+ip)

