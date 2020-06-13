## MANIPULANDO DATA E HORA:
from datetime import date ## biblioteca de data/hora
from datetime import time, datetime ## mais duas biblioteca.

## Buscando data atual:
data_atual = date.today()
print(data_atual.strftime("%d/%m/%y"))

## Buscando hora:
horario = time(hour=15, minute=32, second=54)
hor_certa = horario.strftime('%H:%M:%S')
print(horario)
print(hor_certa)

## Dados atuais:
hora_now = datetime.now()
print(hora_now)
print(data_atual.strftime('%A:%B:%Y'))
print(data_atual.strftime('%D/%M/%Y  %H:%M:%S'))
print(data_atual.weekday())
tupla = (" Segunda","Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(tupla[data_atual.weekday()])
data_string = "08/05/1988"
data_convert = datetime.strptime(data_string,"%d/%m/%Y")
print(data_convert)

