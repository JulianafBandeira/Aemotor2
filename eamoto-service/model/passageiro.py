from helpers.database import db


class Passageiro(db.Model):
    
    
    __tablename__ = 'tb_passageiro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidadeOrigem = db.Column(db.String(90), nullable=False)
    cidadeDestino = db.Column(db.String(90), nullable=False)
    
    aluno_id = db.Colum(db.Integer, db.ForeignKey('tb_aluno.id'))
    

    
    def __init__(self,aluno,cidadeDestino,cidadeOrigem):
        
        self.aluno = aluno
        self.cidadeOrigem = cidadeDestino
        self.cidadeDestino = cidadeOrigem
        
    def __repr__(self):
        return '<aluno{}, cidadeOrigem{},cidadeDestino{}>'.format(self.aluno,self.cidadeDestino,self.cidadeOrigem)