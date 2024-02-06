from flask import Flask

##crear aplicacion
app = Flask(__name__)

#llamar a las rutas definidas 
from app import routes

#iniciar app
if __name__ == "__main__":
    app.run()