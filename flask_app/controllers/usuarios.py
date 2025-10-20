from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.pelicula import Pelicula
from flask import Blueprint


usuarios_bp = Blueprint('usuarios',__name__)




