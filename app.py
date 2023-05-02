from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint
from controllers.places_controller import places_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(places_blueprint)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
