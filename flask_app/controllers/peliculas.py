from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.pelicula import Pelicula
from flask import Blueprint

peliculas_bp = Blueprint("peliculas", __name__)

@peliculas_bp.route("/nueva")
def nueva():
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else:
        return render_template("nueva.html")
    
@peliculas_bp.route("/crear_peli", methods=["POST"])
def crear_peli():
    datos = {
        "nombre":request.form["nombre"],
        "director": request.form["director"],
        "fecha_estreno": request.form["fecha_estreno"],
        "sinopsis": request.form["sinopsis"],
        "usuarios_id": request.form["usuarios_id"]
    }
    Pelicula.save(datos)
    return redirect("/cine")


@peliculas_bp.route("/cine/ver/<int:id>")
def ver(id):
    if "id" not in session:
        flash("Debes iniciar sesión primero")
        return redirect("/")
    else:
        pelicula= Pelicula.get_one(id)
        print(pelicula)
        return render_template("ver.html", pelicula=pelicula[0])