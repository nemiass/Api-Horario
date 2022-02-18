from flask_restful import Resource, reqparse
from flask import request, jsonify
from src.models.Models import Horario, Curso, db
from src.models.schemas import curso_schema, cursos_schema, horario_schema, horarios_schema, CursoSchema
import requests


class Schedule(Resource):

    # get de horarios, trae todos los horarios, y horaio por id_docente
    def get(self, id: int = None):

        if not id:
            # mostrando todos los horarios
            horario = Horario.query.all()
            res = horarios_schema.dump(horario)
            return {"estado": True, "data": res}, 200

        # Horarios de un docente en especifico
        # Peticion al ENDPOINT del servicio de decente para traer al docente por id_usuario
        endpoint_servicio_profesor = "http://54.176.78.122:5000/api/docentes/user"
        url = f"{endpoint_servicio_profesor}/{id}"
        response = requests.get(url)

        if response.status_code != 200:
            return {
                "estado": False,
                "msg": f"error con id {id} de profesor",
                "msg-servicio-profe": response.json()
            }

        response_profesor = response.json()

        horarios_de_profesor = Horario.query.filter_by(id_profesor=id).all()
        res = {"estado": True, "profesor": response_profesor["user"], "horario": []}
        cs = CursoSchema(only=("nombre", "ciclo"))
        for horario_profesor in horarios_de_profesor:
            res["horario"] \
                .append(horario_schema.dump(horario_profesor) | cs.dump(horario_profesor.curso))

        return jsonify(res)

    # guardando un horario en la bd
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"estado": False, "msg": "no input data"}, 400

        validate = horario_schema.validate(json_data)
        if validate:
            return {"estado": False, "msg": validate}, 400

        try:
            new_horario = Horario(
                json_data["day"],
                json_data["time_start"],
                json_data["time_end"],
                json_data["id_profesor"],
                json_data["id_curso"]
            )
            db.session.add(new_horario)
            db.session.commit()
            res = {"estado": True, "data": horario_schema.dump(new_horario)}

        except KeyError as e:
            res = {"estado": False, "error": f"Error {str(e)} required in json request"}, 400

        except Exception as e:
            res = {"estado": False, "error": type(e).__name__, "msg": str(e)}, 400

        return res

    # eliminando un horario la BD
    def delete(self, id: int = None):
        if id:
            try:
                horario = Horario.query.filter_by(id=id).first()

                if not horario:
                    return {"estado": False, "msg": f"No existe id {id} horario en BD"}, 200

                horario_del = horario_schema.dump(horario)
                Horario.query.filter_by(id=id).delete()
                db.session.commit()
                res = {"estado": True, "data": horario_del}, 200

            except Exception as e:
                res = {"estado": False, "msg": type(e).__name__}, 400

            return res
