from flask_app import app
from flask import render_template
from flask_app.controllers.usuarios import usuarios_bp
from flask_app.controllers.peliculas import peliculas_bp

app.register_blueprint(usuarios_bp)
app.register_blueprint(peliculas_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)