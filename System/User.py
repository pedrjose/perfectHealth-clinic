import random
from Consulta import *

class User:
    def __init__(self, nome = None, password = None, userId = None):
        self.nome = nome
        self.userId = userId
        self.password = password
        self.consultas = []
        
    def criarConta(self):
        print('\n| CRIAR CONTA |')
        nome = input('Informe seu nome: ')
        password = input('Informe sua senha: ')
        cpf = input('Informe seu CPF: ')
        u = User(nome, password, cpf)
        return u

    def solicitarConsulta(self):
        print('\n| SOLICITAR CONSULTA |')
        data = input('Informe a data da consulta: ')
        horario = input('Informe o horário da consulta: ')
        sintomas = input('Informe os sintomas que está sentindo: ')
        medico = input('Informe o médico que deseja ser atendido: ')
        c = Consulta()
        c.criarConsulta(data, horario, sintomas, medico)
        medico = random.randint(1, 2)
        if medico == 1:
            self.consultas.append(c)
            print('\n< Consulta agendada! >\n')
        else:
            print('\nNão é possível agendar essa consulta no momento.')
            print('Tente novamente com outra data, horário ou médico!\n')
    
    def visualizarConsulta(self):
        if self.consultas:
            for i in range(len(self.consultas)):
                print(f'\n| CONSULTA {i+1} |')
                print(f'DATA: {self.data.consultas[i]}')
                print(f'HORÁRIO: {self.horario.consultas[i]}')
                print(f'MÉDICO: {self.medico.consultas[i]}')
        else:
            print('\nVocê ainda não tem consultas agendadas!\n')