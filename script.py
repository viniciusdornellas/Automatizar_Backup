import os 
import datetime
import shutil

#Função para buscar os dados do arquivo, recebe o caminho e retorna os dados em uma lista
def dados_arquivo(caminho):
    dados = []
    #Laço for para percorrer todos os arquivos do caminho recebido
    for item in os.listdir(caminho):
        arquivo = os.path.join(caminho, item) 
        #Verificar se o item é um arquivo
        if os.path.isfile(arquivo):
            dados_arquivo = {
                "Nome": item,
                "Tamanho:": os.path.getsize(arquivo),
                "Criacao": datetime.datetime.fromtimestamp(os.path.getctime(arquivo)),
                "Data de Modificacao": datetime.datetime.fromtimestamp(os.path.getmtime(arquivo))
            }
            #O resultado de cada laço é armazenado na lista "dados"
            dados.append(dados_arquivo)
    return dados

#Função para escrever em um arquivo. Recebe o caminho como parâmetro 
def escrever_arquivo(caminho):
    #Variável para armazenar os dados da lista em formato de string
    escrever = ""  
    with open (caminho, "w") as registros:
        for item in dados: 
            #Percorre dados de cada arquivo salvo na lista
            for arquivo, valor in item.items(): 
                #Verifica se o dado é do tipo dateimte e os deixa formatados
                if isinstance(valor, datetime.datetime): 
                    valor = valor.strftime("%Y-%m-%d %H:%M:%S") 
                escrever += f"{arquivo}: {valor}\n"
            escrever += f"-"*40+"\n"
        registros.write(escrever)

#Função para verificar data de criação do arquivo
def compara_datas(caminho):
    data_atual = datetime.datetime.now()
    for item in os.listdir(caminho):
        arquivo = os.path.join(caminho, item)
        data_criacao = datetime.datetime.fromtimestamp(os.path.getctime(arquivo))
        diferenca = data_atual - data_criacao
        #Condições para verificar se o arquivo foi criado há mais de 3 dias ou não
        if diferenca.days > 3:
            os.remove(arquivo)
        else:
            shutil.move(arquivo, caminhoBackUp)
            #Chama função passando caminho para escrever no arquivo backupsTo.log
            dados = dados_arquivo(caminhoBackUp)
            escrever_arquivo(caminhoBackUpTo)

#Variáveis que contém os caminhos e permitem fácil alteração sem precisar alterar as linhas de código
caminho = 'home/valcann/backupsFrom'
caminhoBackUp = 'home/valcann/backupsTo'
caminhoBackUpFrom = 'home/valcann/backupsFrom.log'
caminhoBackUpTo = 'home/valcann/backupsTo.log'

#Chama função passando o caminho da pasta backupsFrom
dados = dados_arquivo(caminho)
#Chama função passando caminho para escrever no arquivo backupsFrom.log
escrever_arquivo(caminhoBackUpFrom)

#Chama função para verificar datas dos arquivos na pasta backupsFrom
compara_datas(caminho)

#Chama função passando caminho para escrever no arquivo backupsTo.log
dados = dados_arquivo(caminhoBackUp)
#Chama função passando caminho para escrever no arquivo backupsTo.log
escrever_arquivo(caminhoBackUpTo)