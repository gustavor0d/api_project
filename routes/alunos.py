from flask import Blueprint, jsonify, request
from apis.entities import api_entidades

alunos_bp = Blueprint("alunos", __name__)

alunos = api_entidades["alunos"]

@alunos_bp.route("/alunos", methods=['GET'])
def get_student():
    return jsonify(alunos)

@alunos_bp.route("/alunos/<int:id>", methods=['GET'])
def get_student_id(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)
    return jsonify(erro="aluno nao encontrado"), 400

@alunos_bp.route("/alunos", methods=['POST'])
def create_student():
    novo_aluno = request.json
    if not novo_aluno.get("nome"):
        return jsonify(erro="aluno sem nome"), 400
    if not any(aluno["id"] == novo_aluno["id"] for aluno in alunos):
        alunos.append(novo_aluno)
        return jsonify(message="criado com sucesso")
    return jsonify(erro="id ja utilizada"), 400

@alunos_bp.route("/alunos/<int:id>", methods=['PUT'])
def update_student(id):
    for aluno in alunos:
        if aluno["id"] == id:
            atualizacao = request.json
            if not atualizacao.get("nome"):
                return jsonify(erro="aluno sem nome"), 400
            aluno["nome"] = atualizacao["nome"]
            return jsonify(message="atualizado com sucesso")
    return jsonify(erro="aluno nao encontrado"), 400

@alunos_bp.route("/alunos/<int:id>", methods=['DELETE'])
def delete_student(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify(message="deletado com sucesso")
    return jsonify(erro="aluno nao encontrado"), 400
