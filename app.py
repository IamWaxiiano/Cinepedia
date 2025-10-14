from flask_app import app, render_template
from flask_app.controllers import usuarios

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)