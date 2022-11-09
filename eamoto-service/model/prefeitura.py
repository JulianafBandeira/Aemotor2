from helpers.database import db


class Prefeitura(db.Model):
    
    
    __tablename__ = "tb_prefeitura"
    
    nomePrefeito = db.Column(db.String(100), unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone=db.Column(db.String(120), nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    rota_id = db.Column(db.Integer, db.ForeignKey("tb_rota.id"))
    
    prefeito_child = db.relationship("Prefeito_db", uselist=False)
    cidade_parent = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    gestores = db.relationship('GestorApp_db', backref='GestorApp_db', lazy=True)
    funcionarios = db.relationship('Funcionario_db', backref='Funcionario_db', lazy=True)
    
     
    def __init__(self, telefone,email,nomePrefeito):
        self.email = email
        self.telefone = telefone
        self.nomePrefeito = nomePrefeito

    def __repr__(self):
        return '<email{},telefone{},nomePrefeito>'.format(self.email,self.telefone)