#se importan las librerias a usar en el proyecto
import requests
import configparser

#encargada de gestionar la renderizacion de las vistas 

from flask import Flask, render_template, request

app = Flask(__name__)
#Se inicia la logica de la app

# Esta condicion siempre va indicando 
# if __name__ =="__main__":
#     app.run(debug=True)

#Ruta principal
@app.route ('/')
# aqui va el nombre de la funcion o metodo que gestiona la ruta
def weaher_dashboard():
    return render_template ('home.html')

#Ruta que despliega los resultados
@app.route ('/results')
def render_resullts
    cityname= request.form['cityname']
    
    # Antes de consumir el api
    api = get_api_key();
    
    
    
    

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config ['openweathermap'] ['api']