import sqlite3

conexao = sqlite3.connect('primeiro banco.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf NOT NULL UNIQUE,
               email TEXT NOT NULL UNIQUE
               )""")

# cursor.execute("""INSERT INTO contas_bancarias (
#               titular, saldo, cpf, email ) VALUES
#               ('Pedro', 20000,'08863745821', 'pedrodoscampos@gmail.com')""")
cursor.execute("""UPDATE contas_bancarias
               SET saldo = 2000
               WHERE id = 2""")
cursor.execute("""SELECT * FROM contas_bancarias""")

    # O sinal de '*' significa que o comando vai pegar TODAS as COLUNAS do banco de dados,
    # ou seja, id, titular, saldo, cpf e email
        # O WHERE vai buscar na tabela somente os dados com o parametro em específico que foi passado,
        # (Exemplo 1: "...WHERE id=1" -> como o id é UNICO para cada um, vai somente buscar a coluna com o as informações do "Pedro")
        # (Exemplo 2: "...WHERE saldo >10000" -> vai aparecer somente pessoa com o saldo acima de 10000)

contas=cursor.fetchall()
# pega o resultado do comando acima e trazer para variavel contas
cursor.execute("DELETE FROM contas_bancarias WHERE id=1")

 

for conta in contas:
    id, titular, saldo, cpf, email = conta
    print(f"""Id: {id}
Titular: {titular}
Saldo: {saldo}
CPF: {cpf}
Email: {email}""")
    print("\n")
print(contas)
conexao.commit()
# INTEGER -> inteiro; NOT NULL -> nao pode ficar vazio;
# PRIMARY KEY -> o que vai identificar cada registro;
# AUTOINCREMENT -> adiciona o +1 ao numero de cadastro automaticamente
