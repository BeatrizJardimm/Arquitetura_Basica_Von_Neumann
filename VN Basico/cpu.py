from re import A
from ram import RAM


class CPU:
    def __init__(self, memoria, io):
        self.memoria =  memoria
        self.io = io
    
    def run(self, endereco):
        self.pc = endereco
        self.a = self.memoria.read(self.pc)
        self.b = self.memoria.read(self.pc + 1)

        num = 1
        for i in range(self.a, self.b + 1):
            if self.memoria.write(i, num):
                self.io.output(f"{i} = {num}\n")
            else:
                print(f"endereco {i} invalido!")
                break
            num +=1