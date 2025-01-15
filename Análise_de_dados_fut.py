import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar Dados
df = pd.read_csv('jogadores.csv')

# Inspecionar os dados
print("Visão geral dos dados:")
print(df.head())
print(df.info())
print(df.describe())

# 2. Limpeza de Dados
# Verificar valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Remover valores nulos
df = df.dropna()

# Criar nova coluna de desempenho
df['Desempenho'] = df['Gols'] + df['Assistências']

# 3. Análise Estatística
# Maiores goleadores
print("\nTop 5 maiores goleadores:")
top_goleadores = df.sort_values(by='Gols', ascending=False).head(5)
print(top_goleadores[['Jogador', 'Gols']])

# Desempenho coletivo por time
desempenho_time = df.groupby('Time')[['Gols', 'Assistências']].sum().reset_index()
desempenho_time['Total_Desempenho'] = desempenho_time['Gols'] + desempenho_time['Assistências']
print("\nDesempenho total por time:")
print(desempenho_time.sort_values(by='Total_Desempenho', ascending=False))

# Melhor desempenho médio por jogo
df['Desempenho_por_jogo'] = df['Desempenho'] / df['Partidas']
print("\nTop 5 desempenho médio por jogo:")
print(df[['Jogador', 'Desempenho_por_jogo']].sort_values(by='Desempenho_por_jogo', ascending=False).head(5))

# 4. Visualização de Dados
# Visualizar top 5 goleadores
print("\nGerando gráficos...")
top_goleadores.plot(x='Jogador', y='Gols', kind='bar', title='Top 5 Goleadores', legend=False)
plt.ylabel('Número de Gols')
plt.show()

# Visualizar desempenho dos times
sns.barplot(x='Time', y='Total_Desempenho', data=desempenho_time)
plt.title('Desempenho Total dos Times')
plt.ylabel('Gols + Assistências')
plt.show()

# Visualizar desempenho médio por jogo
top_desempenho = df[['Jogador', 'Desempenho_por_jogo']].sort_values(by='Desempenho_por_jogo', ascending=False).head(5)
top_desempenho.plot(x='Jogador', y='Desempenho_por_jogo', kind='bar', title='Top 5 Desempenho por Jogo', legend=False)
plt.ylabel('Desempenho Médio por Jogo')
plt.show()

