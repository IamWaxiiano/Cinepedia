from flask_app.config.conexion import Conexion

class Pelicula:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.director= data["director"]
        self.fecha_estreno = data["fecha_estreno"]
        self.sinopsis = data["sinopsis"]
        self.usuario_id = data["usuarios_id"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO pelicula (nombre, apellido, email, password) VALUES (%(nombre)s, %(director)s, %(fecha_estreno)s, %(sinopsis)s, %(usuarios_id)s);"
        return Conexion('cinepedia').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query= "SELECT * from peliculas"
        peliculas_en_bd= Conexion('cinepedia').query_db(query)
        peliculas=[]
        for pelicula in peliculas_en_bd:
            peliculas.append(cls(pelicula))
        return peliculas