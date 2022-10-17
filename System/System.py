from User import *

class System(User):
    def __init__(self):
        self.clientes = []

    def addPaciente(self, cliente):
        self.clientes.append(cliente)

    def fazerLogin(self):
        cpf = input('Informe seu CPF: ')
        password = input('Informe sua senha: ')
        for i in range(len(self.clientes)):
            if self.userId.clientes[i] == cpf and self.password.clientes[i] == password:
                print('< Login bem sucedido! >')
                return True
        print('Algo deu errado. Tente novamente!')
        return False

    def buscarCliente(self, num):
        cpf = input('Informe seu CPF: ')
        for i in range(len(self.clientes)):
            if self.userId.clientes[i] == cpf and num == 1:
                self.userId.clientes[i].visualizarConsulta
            elif self.userId.clientes[i] == cpf and num == 2:
                self.userId.clientes[i].solicitarConsulta()

    def recuperarConta(self):
        cpf = input('Informe seu CPF: ')
        for i in range(len(self.clientes)):
            if self.userId.clientes[i] == cpf:
                print(f'A senha cadastrada para esse CPF é [{self.password.clientes[i]}].')