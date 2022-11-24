#importar o pessoa.py()
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#exemplo de uso()
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

print("\nAcesso ao banco: ")

db = Database()

#instancia o objeto 
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#quero criar uma lista com o que veio do banco de dador
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)


#criar um ob com qualquer diretoretc()
novo = Pessoa(0, "DANZEL WASHINGTON")


novo = pessoaDAO.save(novo)

#consulta o banco
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)




