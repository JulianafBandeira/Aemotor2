from helpers.database import db


class Rota(db.Model):
    
    __tablename__ = 'tb_Rota'

    id = db.Column(db.Integer, primary_key=True)
    nomeDestino = db.Column(db.String(30), nullable=False)
    qtdalunos = db.Column(db.String(11), nullable=False)
    prefeitura = db.Column(db.String(80), nullable=False)
    veiculo = db.Column(db.String(30), nullable=False)
    passageiro = db.Column(db.String(11), nullable=False)
    horaSaida = db.Column(db.String(80), nullable=False)
    horaChegada = db.Column(db.String(80), nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey('Alunos.id'), nullable=False)
    
    prefeitura_child = db.relationship("Prefeitura", uselist=False)
    institutos = db.relationship('InstituicaoDeEnsino', backref='InstituicaoDeEnsino')
    
    def __init__(self, nomeDestino, prefeitura, qtdalunos,veiculo,passageiro,horaSaida,horaChegada):
        self.nomeDestino = nomeDestino
        self.prefeitura = prefeitura
        self.qtdalunos = qtdalunos
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada =  horaChegada
    
    def __repr__(self):

        return '<prefeitura{}, nomeDestino{},qtdalunos{},veiculo{},passageiro{},horaSaida{}, horaChegada{}>'.format(self.prefeitura,self.nomeDestino,self.qtdalunos,self.veiculo,self.passageiro,self.horaSaida,self.horaChegada)