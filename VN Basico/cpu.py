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
            try:
                self.memoria.write(i, num)
                self.io.output(f'> {i} = {num}\n')
            except:
                self.io.output(f"Endereco invalido: {i}")
                break
            num += 1