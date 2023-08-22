from abc import abstractmethod

class EnderecoInvalido(Exception):
  def __init__(self, endereco):
    self.endereco = endereco
  def __str__(self):
    return f"Endereco {self.endereco} invalido. Finalizando o programa."

class Memoria:
  def __init__(self, capacidade):
    self.capacidade = capacidade

  def verifica_endereco(self, endereco):
    if (endereco < 0) or (endereco >= self.capacidade):
      return False
    else:
      return True
  
  def tamanho(self):
    return self.capacidade
  # métodos abstratos devem ser sobrescritos pelas subclasses
  @abstractmethod
  def read(self, endereco): pass

  @abstractmethod
  def write(self, endereco, val): pass