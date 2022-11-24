class Pessoa:
  #Atributos
  id = None
  nome = None
  
  #metodo construtor
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
    #metodo para ajudar na exibiçao
  def __str__(self):
    return f"{self.nome} ({self.id})"
