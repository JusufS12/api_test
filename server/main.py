from flask import Flask, jsonify
from flask_cors import CORS
from testspeed import test_speed

app = Flask(__name__)
CORS(app)


################# ROUTING #################

@app.route('/api/data', methods=['GET'])
def get_data():
  return jsonify({'message': 'Hello from Flask!'})

@app.route('/api/speedtest', methods=['GET'])
def get_speed():
  down_speed, up_speed = test_speed()
  return jsonify({'download': str()})
