from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Horario(db.Model):
    __tablename__ = "horarios"

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(10), nullable=False)
    time_start = db.Column(db.String(20), nullable=False)
    time_end = db.Column(db.String(20), nullable=False)

    id_profesor = db.Column(db.Integer, nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=True)
    curso = db.relationship('Curso', backref=db.backref('horarios'))

    def __init__(self,
        day: str,
        time_start: int,
        time_end: str,
        id_profesor: int,
        id_curso: int
    ) -> None:
        self.id_profesor = id_profesor
        self.day = day
        self.time_start = time_start
        self.time_end = time_end
        self.id_curso = id_curso


class Curso(db.Model):
    __tablename__ = "cursos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    ciclo = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre: str, ciclo: int) -> None:
        self.nombre = nombre
        self.ciclo = ciclo
