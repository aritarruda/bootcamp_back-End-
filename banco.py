#exercicio 01
#Crie uma tabela chamada"alunos"com os seguintes campos:
#id(inteiro),nome(texto),idade(inteiro)e curso(texto)
import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#result = cursor.execute('CREATE TABLE alunos(id INTEGER, nome VARCHAR(100),idade INTEGER, curso VARCHAR(100))')

#for item in result:
    #print(item)

conexao.commit()
conexao.close

#exercicio 02
#Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#result = cursor.execute(''insert into alunos (id, nome, idade, curso) values 
#(1, 'Ana', 30, 'Python'),
#(2, 'Joana', 15, 'Engenharia'),
#(3, 'Maria', 20, 'Engenharia'),
#(4, 'Gabriela', 28, 'Dados'),
#(5, 'Adriana', 36, 'Django')'')


'''exercicio 03
Escreva consultas SQL para realizar as seguintes tarefas:
a)Selecionar todos os registros da tabela"alunos".
b)Selecionar o nome e a idade dos alunos com mais de 20anos.
c)Selecionar os alunos do curso de"Engenharia"em ordem alfabética.
d)Contar o número total de alunos na tabela.'''
#result = cursor.execute('''select * from alunos''')
#result = cursor.execute('''select nome, idade from alunos where idade > 20''')
#result = cursor.execute('''select * from alunos where curso ='Engenharia' order by nome ''')
#result = cursor.execute('''select count(*) from alunos ''')

'''exercicio 04
Atualize a idade de um aluno específico na tabela.
Remova um aluno pelo seu ID'''
#result = cursor.execute('''update alunos set idade = 28 where id = 1''')
#result = cursor.execute('''delete from alunos where id = 1 ''')

#exercicio 05
'''Crie uma tabela chamada"clientes" com os campos:
id(chave primaria),nome(texto),idade(inteiro)e saldo(float).
Insira alguns registros de clientes na tabela'''
#result = cursor.execute('CREATE TABLE clientes(id INTEGER primary Key, nome VARCHAR(100),idade INTEGER, saldo float)')
#result = cursor.execute(''insert into clientes (id, nome, idade, saldo) values 
#(1, 'Ana', 30, 500),
#(2, 'Joana', 15, 1200),
#(3, 'Maria', 20, 3000),
#(4, 'Gabriela', 28, 400),
#(5, 'Adriana', 36, 1000)'')

#exercicio 06
'''Escreva consultas SQL para realizar as seguintes tarefas:
Selecione o nome e a idade dos clientes com idade superior a 30anos.
Calcule o saldo médio dos clientes.
Encontre o cliente com o saldo máximo.
Conte quantos clientes têm saldo acima de 1000'''
#result = cursor.execute('''select nome, idade from clientes where idade > 30''')
#result = cursor.execute('''select AVG(saldo) from clientes''')
#result = cursor.execute('''select nome from clientes where saldo =(select max (saldo) from clientes)''')
#result = cursor.execute('''select count(*) from clientes where saldo > 1000 ''')

#exercicio 07
'''Atualize o saldo de um cliente específico.
Remova um cliente pelo seu ID'''
#result = cursor.execute('''update clientes set saldo = 3500 where id = 1''')
#result = cursor.execute('''delete from clientes where id = 1 ''')

#exercicio 08
'''Crie uma segunda tabela chamada"compras"com os campos:
id(chave primária),cliente_id(chave estrangeira referenciando o id da tabela"clientes"),produto(texto)e valor(real).
Insira algumas compras associadas a clientes existentes na tabela"clientes".
Escreva uma consulta para exibir o nome do cliente,o produto e o valor de cada compra.'''
#result = cursor.execute('CREATE TABLE compras(id INTEGER primary Key, cliente_id INTEGER,produto VARCHAR(100),valor float,CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id))')
#result = cursor.execute(''insert into compras(id, cliente_id, produto, valor) values 
#(1, 1, 30, 'lapis', 3.0),
#(2, 1, 15, 'caderno', 15.0),
#(3, 2, 20, 'borracha', 5.5),

result = cursor.execute('''select c.nome, co.produto, co.valor from compras as co inner join clientes as c on c.id = co.cliente_id''')
for item in result:
    print(item)

conexao.commit()
conexao.close


