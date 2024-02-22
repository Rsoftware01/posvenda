import pandas as pd
from datetime import datetime, timedelta

# Caminho do arquivo Excel
excel_file = "fixing.xlsx"

try:
    # Leitura do arquivo Excel com a linha 0 como nome das colunas
    df = pd.read_excel(excel_file, header=0)

    # Obtendo a data atual
    data_atual = datetime.now()

    # Lista para armazenar os DataFrames filtrados para cada dia
    dfs = []

    # Iterando para os próximos 5 dias
    for i in range(6):  # 6 para incluir o dia atual e os próximos 5 dias
        # Calculando a data para o dia atual mais i dias
        data_filtrada = data_atual + timedelta(days=i)
        # Obtendo a data formatada (dia/mês/ano) para a comparação
        data_formatada = data_filtrada.strftime('%d/%m/%Y')
        # Filtrando o DataFrame para exibir apenas as linhas onde o "Fixing" é igual à data formatada
        df_filtrado = df[df['Fixing'] == data_formatada]
        # Adicionando o DataFrame filtrado à lista
        dfs.append(df_filtrado)

    # Concatenando todos os DataFrames filtrados em um único DataFrame
    df_resultado = pd.concat(dfs)

    # Ordenando o DataFrame pelo nome do operador(a)
    df_resultado = df_resultado.sort_values(by='Operador(a)')

    # Adicionando a coluna "Data hoje" com o mesmo dia e mês da data atual e o ano 2023
    df_resultado["Data hoje"] = data_atual.strftime("%d/%m/2023")

    # Salvando o DataFrame como um arquivo JSON, substituindo os dados existentes
    df_resultado.to_json("data.json", orient='records')
    print("Dados salvos com sucesso no arquivo 'data.json'.")
except FileNotFoundError:
    # Se o arquivo Excel não for encontrado, crie um JSON com a mensagem adequada
    print("Arquivo Excel não encontrado. Criando um JSON com a mensagem 'Sem dados'.")
    with open("data.json", "w") as json_file:
        json_file.write('[{"Mensagem": "Sem dados"}]')
