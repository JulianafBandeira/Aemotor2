
from helpers.database import db

class Endereco(db.Model):
    
    
    __tablename__ = "tb_endereco"
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(30), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    instituicao_id = db.Column(db.Integer, db.ForeignKey("tb_instituicaoDeEnsino.id"))
    pessoa = db.relationship("Pessoa_db")
    
     
    def __init__(self,numero, cep, logradouro,complemento):
        self.cep = cep
        self.numero = numero
        self.logradouro = logradouro
        self.complemento = complemento
        
    def __repr__(self):
       return '<logradouro{},cep{},numero{},complemento{}>'.format(self.logradouro,self.cep,self.complemento,self.numero)