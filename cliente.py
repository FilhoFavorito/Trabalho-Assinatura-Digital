# Criar conta e depois Transação
import json

# Criar conta e depois Transação
import json

import json
import os

def criarConta():
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome completo: ")
    senha = input("Crie sua senha: ")
    saldo = 1000

    novo_cliente = {
        "nome": nome,
        "senha": senha,
        "saldo": saldo
    }

    # Carrega os dados existentes
    if os.path.exists("clientes.json"):
        with open("clientes.json", "r", encoding="utf-8") as file:
            dados = json.load(file)
    else:
        dados = {}

    # Verifica se o CPF já está cadastrado
    if cpf in dados:
        print("⚠️  Já existe uma conta com esse CPF.")
        return

    # Adiciona novo cliente
    dados[cpf] = novo_cliente

    # Salva os dados atualizados
    with open("clientes.json", "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

    print("✅ Conta criada com sucesso!")



def logarConta():
    pass

def fazerTransacao():
    pass

criarConta()


def logarConta():
    pass

def fazerTransacao():
    pass

criarConta()

