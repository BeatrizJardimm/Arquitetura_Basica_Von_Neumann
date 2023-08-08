class IO:
    def __init__(self, entrada, saida):
        self.entrada = entrada
        self.saida = saida

    def output(self, msg):
        print(msg, file=self.saida, end='')