class CPU:
    def __init__(self, memoria, io):
        self.memoria =  memoria
        self.io = io
    
    def run(self, endereco):
        self.pc = endereco
        self.a = self.memoria.read(self.pc)
        self.b = self.memoria.read(self.pc + 1)
        self.c = self.memoria.read(self.pc + 2)

        while self.a <= self.b:
            self.memoria.write(self.a, self.c)
            self.io.output(f'> {self.a} = {self.c}\n')
            self.c += 1
            self.a += 1