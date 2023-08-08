from sys import stdin, stdout
from es import IO
from ram import RAM
from cpu import CPU

def main():
    io = IO(stdin, stdout)
    ram = RAM(7)
    cpu = CPU(ram, io)
    # carrega programa na memoria
    ram.write(10, 120) #(endereco, valor)
    ram.write(11, 130) #vai quebrar pq o maximo e 127
    cpu.run(10)

if __name__ == '__main__':
    main()