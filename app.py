from flask import Flask

#crear instancia
app = Flask(__name__)

#Ruta raiz
@app.route('/')
def hola_mundo():
    return 'Hola mundo'

#Ruta /alumnos
@app.route('/alumnos')
def getAlumnos():
    return 'Aqui van los alumnos'

if __name__ == '__main__':
    app.run(debug=True)

#source bin/activate
#pip install -r requirements.txt
#flask run --port=5010