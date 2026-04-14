import sqlite3

conexao= sqlite3.connect('mercado.db')
cursor=conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS registro( 
               nome TEXT PRIMARY KEY,
               preco_unit FLOAT NOT NULL,
               quantidade INTEGER
               )""")


conexao.commit()