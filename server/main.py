from flask import Flask, jsonify, request
from flask_cors import CORS
from testspeed import test_speed
from threading import Thread
import time

app = Flask(__name__)
CORS(app)


latest_speed = {'download': 0, 'upload': 0}


def update_speed():
  global latest_speed
  while True:
    down_speed, up_speed = test_speed()
    latest_speed = {
      'download': str(down_speed),
      'upload': str(up_speed)
    }
    time.sleep(600)





################# ROUTING #################

@app.route('/api/data', methods=['GET'])
def get_data():
  return jsonify({'message': 'Hello from Flask!'})

@app.route('/api/speedtest', methods=['GET'])
def get_speed():
  return jsonify(latest_speed)





if __name__ == '__main__':
    print("[Flask] Starting server...")
    Thread(target=update_speed, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
