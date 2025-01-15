import pandas as pd
import random

#gerar dados aleatórios 
jogadores = [f'Jorgador {i}' for i in range(1, 51)] #50 jogadores aleatórios
times = ['Time A', 'Time B', 'Time C', 'Time D'] #4 times aleatórios      
dados = {
    'Jogador': jogadores,
    'Time': [random.choice(times) for _ in jogadores],
    'Partidas' : [random.randint(20, 30) for _ in jogadores], 
    'Gols': [random.randint(0, 40) for _ in jogadores],	
    'Assistências': [random.randint(0, 20) for _ in jogadores],
    'Minutos_jogados': [random.randint(1500, 3000) for _ in jogadores],
}


#cria o DataFrame

df = pd.DataFrame(dados)

#salvar como CVS
df.to_csv('jogadores.csv', index=False) 

print("Conjunto de dados criado e salvo como 'dados_futebol.cvs'")