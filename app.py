# 1. Importar la clase Flask desde la librería flask
from flask import Flask


app = Flask(__name__)


@app.route('/')
def saludo():
   
    return '<h1>Saludos, Slack fue exitoso</h1>'

def saludo2():
   
    return '<h2>Esto es una segunda prueba de Slack</h2>'

if __name__ == '__main__':
   
    # Por defecto, se ejecutará en http://127.0.0.1:5000/
    app.run(host="0.0.0.0", port=5000, debug=True)
