# pip install pytz manipular timezones

from datetime import datetime
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)

# usando sem pytz
# data_e_hora_atuais = datetime.now() 
# data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')


# print(data_e_hora_em_texto)

# Convertendo uma string em datetime
# data_e_hora_em_texto = ‘01/03/2018 12:30’
# data_e_hora = datetime.strptime(data_em_texto, ‘%d/%m/%Y %H:%M’)