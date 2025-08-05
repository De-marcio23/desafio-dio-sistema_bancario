# desafio dio criando um sistema bancário com python 05/08/2025

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado. Criação de conta cancelada.")
        return None


# INICIALIZAÇÃO
AGENCIA = "0001"
usuarios = []
contas = []
contador_contas = 1

# Menu principal
menu = """

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Criar novo usuário
[5] Criar nova conta
[0] Sair 

=> """

saldo = 1000.0
limite = 700
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ''

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou: O valor informado é inválido.')    

    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')    

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')

    elif opcao == '3':
        print('\n============EXTRATO===================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('======================================')

    elif opcao == '4':
        criar_usuario(usuarios)

    elif opcao == '5':
        nova_conta = criar_conta(AGENCIA, str(contador_contas).zfill(4), usuarios)
        if nova_conta:
            contas.append(nova_conta)
            contador_contas += 1

    elif opcao == '0':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
