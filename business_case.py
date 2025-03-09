#Gerador de arquivos excel
#Este script python busca dados de uma determinada ação na base de dados do Yahoo finanças e então gera um arquivo Excel
import yfinance as yf

def gerar_arquivo_excel(codigo_acao, dt_inicial, dt_final):
    dados = yf.download(codigo_acao, start=dt_inicial, end=dt_final)
    nome_arquivo = f"{codigo_acao}_{dt_inicial}_{dt_final}.xlsx"
    dados.to_excel(nome_arquivo)
    print(f"\nArquivo Excel '{nome_arquivo}' gerado com sucesso!")
    

print("Seja bem vindo(a) ao gerador de arquivo Excel!")
print("----------------------------------------------")
codigo_acao = input("Digite o código da ação: ")
dt_inicial = input("Digite a data inicial (AAAA-MM-DD): ")
dt_final = input("Digite a data final (AAAA-MM-DD): ")

gerar_arquivo_excel(codigo_acao, dt_inicial, dt_final)

