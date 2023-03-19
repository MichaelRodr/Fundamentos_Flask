from flask import Flask,jsonify
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

@app.route('/cursos')
def listar_cursos():
    try:
        cursor = conexion.connetion.cursor()
        sql = "SELECT codigo,nombre,creditos FROM cursos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        print(datos)
        cursos = []
        for fila in datos:
            curso = {'codigo':fila[0], 'nombre':fila[1],'creditos':fila[2]}
            cursos.append(curso)
        return jsonify({'cursos':cursos, 'mensaje': 'cursos listados'})
    except Exception as ex:
        return jsonify('error')
    
def error404(error):
    return '<h1> La pagina no fue encontrada <h1>'

if __name__ == '__main__' :
    app.config.from_object(config['development'])
    app.register_error_handler(404,error404)
    app.run()