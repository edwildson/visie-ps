from flask import Flask, request, jsonify
import pymysql
from flask_sqlalchemy import SQLAlchemy
from config.settings import app, db
from flask_cors import cross_origin

from models import Person as Pessoa  # Importe o modelo Person

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='jobs.visie.com.br',
            database='edwildsonrodrigues',
            port=3306,
            user='edwildsonrodrigues',
            password='ZWR3aWxkc29u',
            charset='',
            cursorclass= pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)

    return conn

@app.route("/api/persons", methods=["GET"])
@cross_origin()
def get_persons():
    try:
        persons = Pessoa.query.all()

        persons_data = [
            person.serialize()
            for person in persons
        ]

        return jsonify(persons_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/persons", methods=["POST"])
@cross_origin()
def create_person():
    try:
        data = request.get_json()
        
        if all(key in data for key in ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao']):
            person = Pessoa(
                nome=data['nome'],
                rg=data['rg'],
                cpf=data['cpf'],
                data_nascimento=data['data_nascimento'],
                data_admissao=data['data_admissao'],
                funcao=data['funcao']
            )
           
            db.session.add(person)
            db.session.commit()
           
            return jsonify({'data': person.serialize(), 'message': 'Person added successfully'}), 201
        else:
            return jsonify({'error': 'All fields are required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/persons/<int:id>", methods=["GET"])
@cross_origin()
def get_person(id):
    try:
        person = Pessoa.query.filter_by(id_pessoa=id).first()

        print("opa")

        if person is not None:
            return jsonify(person.serialize())
    
        return jsonify({'error': 'Person not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/persons/<int:id>", methods=["PATCH"])
@cross_origin(origins='http://localhost:5173')
def update_person(id):
    try:
        data = request.get_json()

        valid_fields = ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao']

        valid_data = {key: value for key, value in data.items() if key in valid_fields}

        if valid_data:
            person = db.session.get(Pessoa, id)

            if person is None:
                return jsonify({'error': "Person not found"}), 404

            for key, value in valid_data.items():
                setattr(person, key, value)

            db.session.commit()

            return jsonify({'data': person.serialize(), 'message': 'Person updated successfully'}), 201
        else:
            return jsonify({'error': 'At least one field to update is required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/persons/<int:id>", methods=["DELETE"])
@cross_origin()
def delete_person(id):
    try:
        person = Pessoa.query.get(id)

        if person is None:
            return jsonify({'error': "Person not found"}), 404

        db.session.delete(person)
        db.session.commit()

        return jsonify({'message': 'Person deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return 'Hello World' 

if __name__ == '__main__':
    app.run(debug=True)