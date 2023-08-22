from sys import stdin, stdout, stderr
from es import IO
from ram import RAM
from cpu import CPU
from cache import CACHE
from memory import EnderecoInvalido

def main():
    # io = IO(stdin, stdout)
    # ram = RAM(7)
    # # cache = CacheSimples(8, ram)
    # cpu = CPU(ram, io)
    # # carrega programa na memoria
    # ram.write(10, 120) #(endereco, valor)
    # ram.write(11, 130) #vai quebrar pq o maximo e 127
    # cpu.run(10)
    try: 
        io = IO(stdin, stdout)
        ram = RAM(7)
        cache = CACHE(8, ram)
        cpu = CPU(cache, io)
    
        inicio = 10
        ram.write(inicio, 118)
        ram.write(inicio + 1, 130)
        cpu.run(inicio)
    except EnderecoInvalido as e:
        print("Endereço inválido:", e.endereco, file=stderr)

if __name__ == '__main__':
    
    main()