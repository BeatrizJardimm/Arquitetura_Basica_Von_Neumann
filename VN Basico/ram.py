class RAM:
    def __init__(self, k):
        self.capacidade = 2**k
        self.dados = [0] * self.capacidade

    def read(self, endereco):
        return self.dados[endereco]

    def write(self, endereco, palavra):
        if endereco > self.capacidade - 1:
            return False
        elif endereco < 0:
            return False
        else:
            self.dados[endereco] = palavra
            return True