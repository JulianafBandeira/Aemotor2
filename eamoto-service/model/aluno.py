from model.pessoa import Pessoa
from helpers.database import db

class Aluno(Pessoa,db.Model):
    
    __tablename__ = 'tb_aluno'
    __mapper_args__ = {'polymorphic_identity': 'aluno', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    instituicaoDeEnsino = db.Column(db.String(80), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    instituicao_child = db.relationship("InstituicaoDeEnsino", uselist=False)
    rotas = db.relationship('Rotas')
    passageiro_child = db.relationship('Passageiro',uselist=False)
    

    def __init__(self, nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, nascimento, email, telefone)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
        self.pessoa = Pessoa
    
    def __repr__(self):
        return '<nome{}nascimento{}email{}telefone{}instituicaoDeEnsino{}curso{}matricula{}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)
