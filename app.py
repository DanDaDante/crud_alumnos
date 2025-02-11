from flask import Flask

#crear instanci
app = Flask(__name__)

#Ruta raiz
@app.route('/')
def hola_mundo():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(debug=True)

#source bin/activate
#pip install -r requirements.txt
#flask run --port=5010