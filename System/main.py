from System import *
from User import *

def menuPaciente(sistema):
    print('\n| PAINEL DO PACIENTE |')
    print('1 - Visualizar Consultas;\n2 - Agendar Consulta;\n3 - Sair.')
    op = int(input('\nInforme o que deseja fazer: '))
    if op == 1:
        sistema.buscarCliente(1)
        menuPaciente(sistema)
    elif op == 2:
        sistema.buscarCliente(2)
        menuPaciente(sistema)
    elif op == 3:
        print('< Saindo... >')
    else:
        print('Algo deu errado. Tente novamente!')

def menuInicial(sistema):
    print('\n| CLÍNICA SAÚDE PERFEITA |')
    print('1 - Fazer Login;\n2 - Criar Conta;\n3 - Recuperar Senha;\n4 - Fechar Sistema.')
    op = int(input('\nInforme o que deseja fazer: '))
    if op == 1:
        if sistema.fazerLogin():
            menuPaciente(sistema)
        else:
            menuInicial(sistema)
    elif op == 2:
        p = User()
        p = p.criarConta()
        sistema.addPaciente(p)
        print('\n< Conta Criada! >')
        menuInicial(sistema)
    elif op == 3:
        sistema.recuperarConta()
    elif op == 4:
        print('Fechando sistema. Obrigado por contatar a Clínica Saúde Perfeita!')
    else:
        print('Algo deu errado. Tente novamente!')
        menuInicial(sistema)

sistema = System()
menuInicial(sistema)
