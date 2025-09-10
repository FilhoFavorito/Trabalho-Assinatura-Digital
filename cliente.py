import json
import os

def gravarDados(dados_cliente,caminho,cpf):
    
    # Carrega os dados existentes
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as file:
            dados = json.load(file)
    else:
        dados = {}


    # Adiciona novo cliente
    dados[cpf] = dados_cliente

    # Salva os dados atualizados
    with open(caminho, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

novo_cliente = {
    "nome":"Gabriel",
    "saldo": 1337
}

cpf = "1234"

gravarDados(novo_cliente, "servidor.json", cpf)
gravarDados(novo_cliente, "cliente.json", cpf)