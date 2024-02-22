import pandas as pd
from datetime import datetime, timedelta
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Caminho do arquivo Excel
excel_file = "fixing.xlsx"

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
    # Obtendo o dia do meio
    dia_meio = data_filtrada.day
    # Filtrando o DataFrame para exibir apenas as linhas onde o dia do meio da coluna "Fixing" é igual ao dia calculado
    df_filtrado = df[df['Fixing'].apply(lambda x: str(x).split("/")[1] if len(str(x).split("/")) >= 3 else None).astype(float) == dia_meio]
    # Adicionando o DataFrame filtrado à lista
    dfs.append(df_filtrado)

# Concatenando todos os DataFrames filtrados em um único DataFrame
df_resultado = pd.concat(dfs)

# Ordenando o DataFrame pelo nome do operador(a)
df_resultado = df_resultado.sort_values(by='Operador(a)')

# Salvando o DataFrame como um arquivo JSON
json_file = "data.json"
df_resultado.to_json(json_file, orient='records')

# Classe para lidar com solicitações HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configuração dos cabeçalhos da resposta
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Leitura do conteúdo do arquivo JSON
        with open(json_file, 'rb') as file:
            content = file.read()
            self.wfile.write(content)

# Função para iniciar o servidor HTTP
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor HTTP rodando na porta {port}')
    httpd.serve_forever()

# Rodando o servidor HTTP
if __name__ == '__main__':
    run()
