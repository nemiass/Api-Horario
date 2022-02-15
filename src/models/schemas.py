from flask_marshmallow import Marshmallow
from marshmallow import fields, Schema

ma = Marshmallow()

class HorarioSchema(ma.Schema):
    class Meta:
        fields = ("id", "day", "time_start", "time_end","id_profesor", "id_curso")
        ordered = True
    #id = fields.Integer(allow)

class CursoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "ciclo")
        ordered = True

horario_schema = HorarioSchema()
horarios_schema = HorarioSchema(many=True)

curso_schema = CursoSchema()
cursos_schema = CursoSchema(many=True)
