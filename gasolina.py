import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o')
plt.title('Preço Médio de Venda da Gasolina em São Paulo (Julho 2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvar o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()