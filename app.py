from flask import Flask, render_template
from routes import get_routes
from stations import get_stations

app = Flask(__name__)

@app.route('/')
def home():
    stations = get_stations()
    routes = get_routes()
    return render_template('home.html', stations=stations, routes=routes)

if __name__ == "__main__":
    app.run(debug=True)
