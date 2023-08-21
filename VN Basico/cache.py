from memory import Memoria
from ram import RAM

class CACHE(Memoria):
    def __init__(self, capacidade, ram: RAM):
        self.capacidade = capacidade
        self.cache = {}
        self.ram = ram

    def read(self, endereco):
        try:
            world = self.cache[endereco]
            print(f'Cache HIT: {world}')

            return world
        except:
            print(f'Cache MISS: {endereco}')
            self.atualizarEnderecoCache(endereco)
            world = self.cache[endereco]

            return world

    def write(self, endereco, world):
        try:
            self.read(endereco)
            self.cache[endereco] = world
        except:
            raise Exception("Finalizar")

    def atualizarEnderecoCache(self, endereco):
        count = 0

        if len(self.cache) > 0:
            for endereco_cache in self.cache:
                self.ram.write(endereco_cache, self.cache[endereco_cache])

        for i in range(endereco, self.ram.capacidade):
            self.cache[i] = self.ram.read(i)
            
            if count > self.capacidade -1:
                break

            count+=1

