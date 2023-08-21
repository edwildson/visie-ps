# import pymysql

# conn = pymysql.connect(
#     host='jobs.visie.com.br',
#     database='edwildsonrodrigues',
#     port=3306,
#     user='edwildsonrodrigues',
#     password='ZWR3aWxkc29u',
#     charset='',
#     cursorclass= pymysql.cursors.DictCursor
# )

# cursor = conn.cursor()

# sql_query = """ CREATE TABLE IF NOT EXISTS pessoas(
#   `id_pessoa` TINYINT(255) NOT NULL AUTO_INCREMENT,
#   `nome` CHAR(100) NOT NULL,
#   `rg` CHAR(100) NOT NULL,
#   `cpf` CHAR(100) NOT NULL,
#   `data_nascimento` DATE NOT NULL,
#   `data_admissao` DATE NOT NULL,
#   `funcao` CHAR(100) NULL,
# PRIMARY KEY (`id_pessoa`)
# )
# """

# cursor.execute(sql_query)
# conn.close()

# print("Processo finalizado")

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person
from config.settings import app, db



# Criação da tabela, caso não exista
with app.app_context():
    Session = sessionmaker(bind=db.engine)
    db.create_all()

# Dados para inserção
dados = [
    {'nome': 'Alberto Vieira', 'rg': '25.507.105-2', 'cpf': '168.637.122-53', 'data_nascimento': date(1997, 7, 1), 'data_admissao': date(2020, 9, 28), 'funcao': None},
    {'nome': 'Alexandre Teixeira', 'rg': '79.474.888-8', 'cpf': '877.733.889-89', 'data_nascimento': date(1982, 8, 16), 'data_admissao': date(2020, 5, 15), 'funcao': None},
    {'nome': 'Ana Carolina Souza', 'rg': '52.565.667-8', 'cpf': '766.370.920-96', 'data_nascimento': date(1982, 3, 19), 'data_admissao': date(2016, 8, 19), 'funcao': None},
    {'nome': 'Ana Paula Soares', 'rg': '54.744.331-9', 'cpf': '746.917.734-52', 'data_nascimento': date(1984, 9, 1), 'data_admissao': date(2019, 8, 25), 'funcao': None},
    {'nome': 'Antônio Siqueira', 'rg': '81.669.888-5', 'cpf': '695.991.412-45', 'data_nascimento': date(1990, 7, 26), 'data_admissao': date(2016, 5, 18), 'funcao': None},
    {'nome': 'Arthur Silva', 'rg': '43.204.402-9', 'cpf': '345.898.157-88', 'data_nascimento': date(1996, 12, 30), 'data_admissao': date(2016, 4, 28), 'funcao': None},
    {'nome': 'Bárbara Santos', 'rg': '57.106.623-3', 'cpf': '587.914.225-66', 'data_nascimento': date(2000, 9, 4), 'data_admissao': date(2018, 11, 17), 'funcao': None},
    {'nome': 'Beatriz Santana', 'rg': '70.855.305-2', 'cpf': '093.084.203-04', 'data_nascimento': date(1994, 5, 17), 'data_admissao': date(2018, 3, 5), 'funcao': None},
    {'nome': 'Caio Sampaio', 'rg': '14.475.327-9', 'cpf': '483.764.953-05', 'data_nascimento': date(1995, 11, 18), 'data_admissao': date(2020, 6, 3), 'funcao': None},
    {'nome': 'Carla Rodrigues', 'rg': '62.692.082-5', 'cpf': '566.412.961-13', 'data_nascimento': date(1996, 8, 4), 'data_admissao': date(2015, 3, 31), 'funcao': None},
    {'nome': 'Carlos Rocha', 'rg': '23.782.125-5', 'cpf': '053.166.034-60', 'data_nascimento': date(1983, 7, 7), 'data_admissao': date(2017, 3, 8), 'funcao': None},
    {'nome': 'Cauê Ribeiro', 'rg': '33.548.790-1', 'cpf': '491.145.149-15', 'data_nascimento': date(1981, 1, 27), 'data_admissao': date(2020, 12, 31), 'funcao': None},
    {'nome': 'Cláudia Reis', 'rg': '54.435.082-9', 'cpf': '511.020.782-80', 'data_nascimento': date(1986, 8, 4), 'data_admissao': date(2020, 9, 25), 'funcao': None},
    {'nome': 'Cláudio Ramos', 'rg': '41.432.308-6', 'cpf': '673.452.026-90', 'data_nascimento': date(1982, 8, 12), 'data_admissao': date(2019, 11, 1), 'funcao': None},
    {'nome': 'Daiane Pereira', 'rg': '90.815.741-8', 'cpf': '704.352.424-58', 'data_nascimento': date(2002, 11, 22), 'data_admissao': date(2017, 6, 15), 'funcao': None},
    {'nome': 'Diego Penha', 'rg': '43.099.953-1', 'cpf': '329.630.074-00', 'data_nascimento': date(1983, 2, 23), 'data_admissao': date(2017, 12, 1), 'funcao': None},
    {'nome': 'Eduardo Oliveira', 'rg': '46.249.609-1', 'cpf': '772.220.114-80', 'data_nascimento': date(2001, 2, 12), 'data_admissao': date(2020, 5, 10), 'funcao': None},
    {'nome': 'Eliana Nunes', 'rg': '84.269.396-7', 'cpf': '130.491.959-59', 'data_nascimento': date(1994, 7, 3), 'data_admissao': date(2018, 1, 16), 'funcao': None},
    {'nome': 'Enzo Nascimento', 'rg': '68.986.227-4', 'cpf': '356.759.355-25', 'data_nascimento': date(1989, 5, 5), 'data_admissao': date(2016, 8, 23), 'funcao': None},
    {'nome': 'Fabiana Moura', 'rg': '69.437.526-9', 'cpf': '149.992.262-00', 'data_nascimento': date(1995, 8, 21), 'data_admissao': date(2019, 3, 26), 'funcao': None},
]

# Inserir os dados
with app.app_context():
    with Session() as session:
        for dado in dados:
            person = Person(**dado)
            session.add(person)
        session.commit()