"""
Criar um sistema implementando depósito, saque e apresentação de extrato

Depósito -> somente valores positivos -> armazenar depósitos em variável

Saque -> Somente 3 saques diários com limite de 500 por saque. -> Caso não tenha limite informar mensagem
-> deve ser armazenado em variável

Extrato -> Deve listar depósitos e saques. -> Deve ser exibido o valor atual da conta. -> Se não for realizado
nenhuma operação: exibir mensagem 'Não foram realizadas movimentações.

-> Deve ser exibidor o valor com duas casas decimais

"""

import textwrap

menu = """
        [d] Depositar
        [s] Saque
        [e] Extrato
        [cu] Criar novo usuário
        [lc] Listar Contas
        [nc] Nova Conta
        [q] Sair
        
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_deposito = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"


def depositar(saldo, deposito, extrato):
    if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$: {deposito:.2f}\n'
    else:
        print('Valor inválido para operação. Por favor digite válido: ')

    return saldo, extrato

def sacar(*, saldo, saque, numero_saques, extrato):  
    if saque > saldo:
            print('Valor não pode ser sacado. Saldo indisponível !')
    elif saque > 500:
            print('Valor sacado deve ser menor que R$ 500.00 !')
    elif saque > 0:
            numero_saques +=1
            if numero_saques > LIMITE_SAQUES:
                print('Saques diários excedidos !')
            else:
                saldo -= saque
                extrato += f'Saque: R$: {saque:.2f}\n'
    else:
            print('Valor inválido para operação')
    
    return saldo, extrato

def exibir_extrato(saldo, extrato= extrato):
    print('==================EXTRATO======================')
    print('Não foram realizadas operações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('===============================================')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
   

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input('Insira o valor a ser depositado: '))
        saldo, extrato = depositar(saldo, deposito, extrato)
        

    elif opcao == "s":
        saque = float(input('Digite o valor a ser sacado: '))
        saldo, extrato = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                numero_saques=numero_saques,
                )
               
    elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
            criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        break
    else:
        print('Operação inválida. Por favor selecione novamente a opção desejada !')