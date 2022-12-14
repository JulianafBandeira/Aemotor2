from helpers.database import db


class Cidade(db.Model):
    
    __tablename__ = 'tb_cidade'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(90), nullable=False)
    sigla = db.Column(db.String(6), nullable=False)
    
    prefeitura_child = db.relationship("Prefeitura", uselist=False)
    uf_child = db.relationship("Uf_db",backref='Uf_db', lazy=True, uselist=False)
    
    
    
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
    def __repr__(self):
        return '<nome{},sigla{}>'.format(self.nome,self.sigla)