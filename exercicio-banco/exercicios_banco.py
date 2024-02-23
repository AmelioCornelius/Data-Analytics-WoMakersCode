import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#1 - Criação da tabela alunos
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2 - Registros de Alunos
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1, "Pedro", 22, "Odontologia");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2, "Letícia", 20, "Histótória");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3, "Cauã", 25, "Publicidade e Propaganda");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4, "Carla", 26, "Engenharia");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5, "Geovana", 28, "Medicina");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6, "João", 28, "Engenharia");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7, "Isaque", 20, "Engenharia");')

#3 - Consultas Básicas
#3a - Selecionar todos os registros da tabela "alunos"
todos = cursor.execute('SELECT * FROM alunos')
for alunos in todos:
    print(alunos)
#3b - Selecionar o nome e a idade dos alunos com mais de 20 anos
nome_idade = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
for alunos in todos:
    print(alunos)
#3c - Selecionar os alunos do curso de "Engenharia" em ordem alfabética
ordenado = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for alunos in todos:
    print(alunos)
#3d - Contar o número total de alunos na tabela
total_alunos = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in todos:
    print(alunos)

#4 - Atualização e Remoção
#4a - Atualize a idade de um aluno específico na tabela
cursor.execute('UPDATE alunos SET idade=25 WHERE nome="João"')
#4b - Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos WHERE id=7')

#5 - Criar uma Tabela e Inserir Dados
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
#Inserindo registros
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1, "Marcela", 35, 2300.00);')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2, "José", 42, 9300.00);')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3, "Enzo", 19, 321.75);')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4, "Carla", 25, 4750.33);')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5, "Georgina", 20, 275.14);')

#6 - Consultas e Funções Agregadas
#6a -Selecione o nome e a idade dos clientes com idade superior a 30 anos
superior_a_trinta = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
for clientes in superior_a_trinta:
    print(clientes)
#6b - Calcule o saldo médio dos clientes
saldo_medio = cursor.execute('SELECT ROUND(AVG(saldo),2) FROM clientes')
saldo_medio = cursor.fetchall()
print(saldo_medio)
#6c - Encontre o cliente com o saldo máximo
cliente_maior_saldo = cursor.execute('SELECT nome,MAX(saldo) as MAIOR_SALDO FROM clientes')
cliente_maior_saldo = cursor.fetchall()
print(cliente_maior_saldo)
#6d - Conte quantos clientes têm saldo acima de 1000
saldo_acima_mil = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo>1000')
saldo_acima_mil = cursor.fetchall()
print(saldo_acima_mil)

#7 - Atualização e Remoção com Condições
#7a - atualizar o saldo do cliente
cursor.execute('UPDATE clientes SET saldo=750.00 WHERE nome="Georgina"')
#7b - remover um cliente pelo id
cursor.execute('DELETE FROM clientes WHERE id=3')

#8 - Junção de Tabelas
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT,  produto VARCHAR(100), valor REAL, FOREIGN KEY(client_id) REFERENCES clientes(id));')
#Adicionando registros
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 2, "Esmalte Risqué Angélica", "6.15")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 5, "Garrafa 500ml", "20.99")')
#Consulta
compra = cursor.execute('SELECT clientes.nome,compras.produto,compras.valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id ORDER BY clientes.nome, compras.produto')
for compras in compra:
    print(compras)

conexao.commit()
conexao.close