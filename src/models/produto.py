from src.models.user import db

class Produto(db.Model):
    __tablename__ = 'produtos'
    
    codigo = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    
    # Relacionamento com lotes (será definido após importação do modelo Lote)
    # lotes = db.relationship('Lote', backref='produto', lazy=True)
    
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome
        }

