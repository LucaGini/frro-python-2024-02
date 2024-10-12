from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NegocioSocio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'<Socio {self.nombre}>'
