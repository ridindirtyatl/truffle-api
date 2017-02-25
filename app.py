from flask import Flask, send_from_directory, send_file
import wtforms_json
from busid import busid_api
from buses import buses_api
from routeid import routeid_api
from routes import routes_api
import os


app = Flask(__name__)

app.config["WTF_CSRF_ENABLED"] = False
wtforms_json.init()

app.register_blueprint(busid_api)
app.register_blueprint(buses_api)
app.register_blueprint(routeid_api)
app.register_blueprint(routes_api)


@app.route('/apidocs/<path:path>')
def send_js(path):
    return send_from_directory('apidocs', path)


@app.route('/', methods=['GET'])
def home():
    return send_file('index.html')


@app.route('/API.raml', methods=['GET'])
def raml():
    return send_file('API.raml')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
