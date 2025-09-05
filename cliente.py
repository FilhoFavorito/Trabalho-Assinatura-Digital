# Criar conta e depois Transação
import json

def criarConta():

    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome completo: ")
    senha = input("Crie sua senha: ")
    saldo = 1000
    
    dados = {
        "cpf":cpf,
        "nome":nome,
        "senha":senha,
        "saldo":saldo
    }
    
    with open("clientes.json", "w") as file:
        json.dump(dados, file)


def logarConta():
    pass

def fazerTransacao():
    pass

criarConta()

