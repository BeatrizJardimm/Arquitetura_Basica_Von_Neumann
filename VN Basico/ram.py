from memory import Memoria


class RAM(Memoria):
    def __init__(self, k):
        self.capacidade = 2**k
        self.ram = [0] * self.capacidade

    def read(self, endereco):
        super().verifica_endereco(endereco)
        return self.ram[endereco]

    def write(self, endereco, palavra):
        super().verifica_endereco(endereco)
        self.ram[endereco] = palavra
