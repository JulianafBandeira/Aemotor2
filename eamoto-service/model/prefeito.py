from helpers.database import db
from model.pessoa import Pessoa



class Prefeito(Pessoa,db.Model):
    
    
    __tablename__ = 'tb_prefeito'
    __mapper_args__ = {'polymorphic_identity': 'prefeito', 'concrete': True}
    

    id = db.Column(db.Integer, primary_key=True)
    nomePref = db.Column(db.String(80), nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_id = db.Column(db.Integer, db.ForeignKey("tb_prefeitura.id"))
    
    
 
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return 'prefeito{}>'.format(self.pessoa)