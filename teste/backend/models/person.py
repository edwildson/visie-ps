from config.settings import db

class Person(db.Model):
    __tablename__ = 'pessoas'  # Nome da tabela no banco de dados

    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=False, nullable=False)
    cpf = db.Column(db.String(255), unique=False, nullable=False)
    rg = db.Column(db.String(255), unique=False, nullable=False)
    data_nascimento = db.Column(db.Date, unique=False, nullable=False)
    data_admissao = db.Column(db.Date, unique=False, nullable=False)
    funcao = db.Column(db.String(255), unique=False, nullable=True)

    # Constructor if needed
    def __init__(self, nome, rg, cpf, data_nascimento, data_admissao, funcao):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao
        self.funcao = funcao
    
    def __repr__(self):
        return f'<Person {self.nome}>'
    
    def serialize(self):
        return {
            'id': self.id_pessoa,
            'nome': self.nome,
            'rg': self.rg,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento,
            'data_admissao': self.data_admissao,
            'funcao': self.funcao
        }