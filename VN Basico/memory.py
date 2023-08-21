from abc import abstractmethod

class EnderecoInvalido(Exception):
  def __init__(self, ender):
    self.ender = ender
  def __str__(self):
    return f"Endereco {self.ender} invalido. Finalizando o programa."

class Memoria:
  def __init__(self, capacidade):
    self.capacidade = capacidade

  def verifica_endereco(self, ender):
    if (ender < 0) or (ender >= self.capacidade):
      raise EnderecoInvalido(ender)
  
  def tamanho(self):
    return self.capacidade
  # métodos abstratos devem ser sobrescritos pelas subclasses
  @abstractmethod
  def read(self, ender): pass

  @abstractmethod
  def write(self, ender, val): pass