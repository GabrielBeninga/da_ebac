# código de geração do gráfico 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha com a cor vermelha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o', color='red')
plt.title('Preço Médio da Gasolina em São Paulo (Julho 2021)')
plt.xlabel('Day')
plt.ylabel('Price (R$)')

# Salvar o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()