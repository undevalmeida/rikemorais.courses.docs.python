from datetime import datetime, timedelta
from datas_br import DatasBr

'''
hoje = datetime.today()
hoje_formatada = hoje.strftime('%d/%m/%Y %H:%M:%S')
print(hoje)
print(hoje_formatada)
'''

hoje = DatasBr()
print(hoje.tempo_cadastro())