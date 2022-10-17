from dataclasses import dataclass

class Consulta:
    def __init__(self, data = None, horario = None, sintomas = None, medico = None):
        self.data = data
        self.horario = horario
        self.sintomas = sintomas
        self.medico = medico

    def criarConsulta(self, data, horario, sintomas, medico):
        c = Consulta(data, horario, sintomas, medico)
        return c