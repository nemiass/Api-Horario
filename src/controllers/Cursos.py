from flask_restful import Resource
from flask import request
from src.models.Models import Curso, db
from src.models.schemas import curso_schema, cursos_schema


class Cursos(Resource):

    def get(self, id_profesor: int = None):
        cursos = Curso.query.all()
        res = cursos_schema.dump(cursos)
        return {"estado": True, "data": res}, 200
    
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"estado": False, "msg": "no json data"}, 400

        validate = curso_schema.validate(json_data)
        if validate:
            return {"estado": False, "msg": validate}, 400

        try:
            new_curso = Curso(
                json_data["nombre"],
                json_data["ciclo"]
            )
            db.session.add(new_curso)
            db.session.commit()
            res = {"estado": True, "data": curso_schema.dump(new_curso)}

        except KeyError as e:
            res = {"estado": False, "error": f"Error {str(e)} required in json request"}, 400

        except Exception as e:
            res = {"estado": False, "error": type(e).__name__, "msg": str(e)}, 400

        return res
        
