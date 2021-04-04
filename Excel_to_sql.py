# import pandas as pd
# from .models import *

# venda = Venda.objects.all()
# print(venda)

# df = pd.read_sql('select * from automovel", [parametros para conexão])

# df.to_excel("saida.xlsx", index=False)


# valor1 = input('> Digite um numero : ')
# valor2 = input('> Digite um numero : ')
# print(valor1 + valor2)

# valor1  = int(valor1)
# valor2 = int(valor2)
# print(valor1+valor2)

#faca um sistema que peca os seguintes valores (ano, mes, dia)
#NOTA: a variavel mes dever ser uma string escrita o mes
#imprima o seguinte texto "O usuário nasceu no dia &&& no mes &&& do ano &&&"

import pandas as pd
import sqlite3
from datetime import datetime

data = datetime.now()
file_name = 'teste.xlsx' 
df = pd.read_excel(file_name, index_col=0)

connection = sqlite3.connect('teste.sqlite3')
c = connection.cursor()

for i in range(len(df['Unnamed: 1'].values)):
    print(i)
# print(df['Unnamed: 1'].values[27])
    c.execute(f'insert into core_venda(situacao, pagamento, app, cliente, device_ID, device_KEY, tipo) values("Vendido", "100%", "OK", "{str(df["Unnamed: 4"].values[i])}", "{str(df["Unnamed: 2"].values[i])}", "{str(df["Unnamed: 3"].values[i])}", "{str(df["Unnamed: 5"].values[i])}");')
connection.commit()
connection.close()



# def carregardadosexcel(nome_ficheiro):
#     dados = pe.iget_records(file_name=nome_ficheiro)
#     return dados

# dados =  carregardadosexcel('teste.xlsx')
# for i in dados: 
#     print(i['APP PG'])
