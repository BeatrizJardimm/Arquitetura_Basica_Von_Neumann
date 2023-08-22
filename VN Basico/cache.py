from memory import Memoria
from ram import RAM
from memory import EnderecoInvalido

class CACHE(Memoria):
    def __init__(self, capacidade, ram: RAM):
        self.capacidade = capacidade
        self.cache = {}
        self.ram = ram

    def read(self, endereco):
        try:
            word = self.cache[endereco]
            print(f'Cache HIT: {endereco}')

            return word

        except:
            print(f'Cache MISS: {endereco}')
            self.atualizarEnderecoCache(endereco)
            word = self.cache[endereco]
            return word

    def write(self, endereco, word):

        try:
            self.read(endereco)
            self.cache[endereco] = word
        except EnderecoInvalido as e:
            print(f"Erro", e.__str__())

    def atualizarEnderecoCache(self, endereco):
        count = 0

        if len(self.cache) > 0:
            for endereco_cache in self.cache:
                self.ram.write(endereco_cache, self.cache[endereco_cache])

        for i in range(endereco, self.ram.capacidade):
            self.cache[i] = self.ram.read(i)
            
            if count > self.capacidade:
                break

            count+=1

