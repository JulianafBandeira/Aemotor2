from helpers.database import db
from model.motorista import Motorista


class Funcionario(db.Model):
    __tablename__ = "tb_funcionario"
    
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(30), nullable=False)
    prefeitura = db.Column(db.String(90), nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_id = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)
    
    motorista = db.relationship("Motorista_db", uselist=False)
    pessoa = db.relationship("Pessoa_db",foreign_keys=[pessoa_id])
    
    
    def __init__(self, prefeitura, cargo,pessoa):
        self.prefeitura = prefeitura
        self.cargo = cargo
        self.pessoa = pessoa
    
    def __repr__(self):
        return '<prefeitura{},cargo{}>'.format(self.cargo,self.prefeitura)