# Gerador de Informações de Jogadores - Campeonato Brasileiro Série A

## Descrição

A **Análise de Dados Esportivos** é um projeto desenvolvido para coletar, processar e gerar dados sobre os jogadores do Campeonato Brasileiro Série A. O objetivo é fornecer um arquivo `.csv` com estatísticas detalhadas de jogadores, como partidas jogadas, gols, assistências e minutos jogados, além de possibilitar análises mais profundas e comparações entre os atletas.

## Funcionalidades

- **Leitura e Processamento de Dados**: Processa informações sobre jogadores de diferentes times, como:
  - Nome do jogador
  - Time
  - Partidas jogadas
  - Gols marcados
  - Assistências
  - Minutos jogados
- **Exportação de Dados**: Geração de um arquivo `.csv` com os dados processados.
- **Análises Estatísticas** (Opcional): Realiza análises dos dados com base nas métricas mencionadas, podendo gerar gráficos para melhor visualização (com a utilização das bibliotecas Matplotlib ou Seaborn).

## Pré-requisitos

Antes de rodar o projeto, é necessário ter o Python instalado e as seguintes bibliotecas:

- **Pandas** para manipulação de dados
- **Matplotlib** ou **Seaborn** para visualização de gráficos (opcional)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/natanserra/An-lise_de_dados
    cd An-alise_de_dados
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    # Para Linux/Mac
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Como Rodar

Para gerar os dados e visualizar o arquivo CSV:

```bash
python Análise_de_dados_fut.py
