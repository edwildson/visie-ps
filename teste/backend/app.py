from flask import Flask, request, jsonify
import json
import pymysql


app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='',
            database='',
            port=3306,
            user='',
            password='',
            charset='',
            cursorclass= pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)

    return conn

@app.route("/persons", methods=["GET"])
def get_persons():
    try:
        conn = db_connection()
        
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pessoas")

            persons = [
                dict(
                    id=row['id_pessoa'],
                    name=row['nome'],
                    rg=row['rg'],
                    cpf=row['cpf'],
                    birth_date=row['data_nascimento'],
                    hire_date=row['data_admissao'],
                    role=row['funcao']
                ) for row in cursor.fetchall()
            ]

            conn.close()

            return jsonify(persons)
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
            

@app.route("/persons", methods=["POST"])
def create_person():
    try:
        data = request.get_json()
        
        if all(key in data for key in ['name', 'rg', 'cpf', 'birth_date', 'hire_date', 'role']):
            conn = db_connection()

            with conn.cursor() as cursor:
                sql = "INSERT INTO pessoas (nome, rg, cpf, data_nascimento, data_admissao, funcao) VALUES (%s, %s, %s, %s, %s, %s)"
                
                cursor.execute(sql, (
                    data['name'], 
                    data['rg'], 
                    data['cpf'], 
                    data['birth_date'], 
                    data['hire_date'], 
                    data['role']
                ))
                
                conn.commit()
            conn.close()
            return jsonify({'message': 'Person added successfully'}), 201
        else:
            return jsonify({'error': 'All fields are required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/persons/<int:id>", methods=["GET"])
def get_person(id):
    try:
        conn = db_connection()

        with conn.cursor() as cursor:
            sql = "SELECT * FROM pessoas WHERE id_pessoa = %s"
            cursor.execute(sql, (id,))
            data = cursor.fetchone()

            person = dict(
                id=data['id_pessoa'],
                name=data['nome'],
                rg=data['rg'],
                cpf=data['cpf'],
                birth_date=data['data_nascimento'],
                hire_date=data['data_admissao'],
                role=data['funcao']
            ) 

        conn.close()

        if person is not None:
            return jsonify(person)
    
        return jsonify({'error': 'Person not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/persons/<int:id>", methods=["PATCH"])
def update_person(id):
    try:
        data = request.get_json()

        valid_fields = ['nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao']

        valid_data = {key: value for key, value in data.items() if key in valid_fields}

        if valid_data:
            conn = db_connection()

            with conn.cursor() as cursor:
                update_values = ', '.join([f"{key} = %s" for key in valid_data.keys()])
                sql = f"UPDATE pessoas SET {update_values} WHERE id_pessoa = %s"
                cursor.execute(sql, (*valid_data.values(), id))
                conn.commit()

            conn.close()

            return jsonify({'message': 'Person updated successfully'}), 200
        else:
            return jsonify({'error': 'At least one field to update is required'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/persons/<int:id>", methods=["PATCH"])
def delete_person(id):
    try:
        conn = db_connection

        with conn.cursor() as cursor:
            sql = "DELETE FROM pessoas WHERE id_pessoa = %s"
            cursor.execute(sql, (id,))
            conn.commit()

        conn.close()

        return jsonify({'message': 'Person deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return 'Hello World' 

if __name__ == '__main__':
    app.run(debug=True)
