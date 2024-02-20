import pandas as pd

# Caminho do arquivo Excel
excel_file = "fixing.xlsx"

# Leitura do arquivo Excel
df = pd.read_excel(excel_file)

# Imprimindo os dados da tabela
print(df)
