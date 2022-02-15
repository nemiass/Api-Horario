from flask_restful import Api
from .controllers.Schedule import Schedule
from .controllers.Cursos import Cursos


api = Api()

# my resources
api.add_resource(Schedule, "/api/horario", "/api/horario/<int:id>", endpoint="horario")
api.add_resource(Cursos, "/api/cursos", "/api/cursos/<int:id>", endpoint="cursos")
