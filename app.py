from flask_app import app
from flask_app.controllers import usuarios
from flask import render_template
from flask_app.controllers.usuarios import usuarios_bp

app.register_blueprint(usuarios_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)