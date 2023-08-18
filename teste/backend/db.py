import pymysql

conn = pymysql.connect(
    host='',
    database='',
    port=3306,
    user='',
    password='',
    charset='',
    cursorclass= pymysql.cursors.DictCursor
)

cursor = conn.cursor()

sql_query = """ CREATE TABLE IF NOT EXISTS pessoas(
  `id_pessoa` TINYINT(255) NOT NULL AUTO_INCREMENT,
  `nome` CHAR(100) NOT NULL,
  `rg` CHAR(100) NOT NULL,
  `cpf` CHAR(100) NOT NULL,
  `data_nascimento` DATE NOT NULL,
  `data_admissao` DATE NOT NULL,
  `funcao` CHAR(100) NULL,
PRIMARY KEY (`id_pessoa`)
)
"""

cursor.execute(sql_query)
conn.close()

print("Processo finalizado")
