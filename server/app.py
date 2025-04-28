from flask import Flask, jsonify, request
from flask_cors import CORS
from threading import Thread
import time
from dotenv import load_dotenv
import os
# from testspeed import test_speed
# from scrape import scrape_books

app = Flask(__name__)
CORS(app)

load_dotenv()
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')


# latest_speed = {'download': 0, 'upload': 0}


# def update_speed():
#   global latest_speed
#   while True:
#     down_speed, up_speed = test_speed()
#     latest_speed = {
#       'download': str(down_speed),
#       'upload': str(up_speed)
#     }
#     time.sleep(600)





################# ROUTING #################

@app.route('/api/data', methods=['GET'])
def get_data():
  return jsonify({'message': 'Hello from Flask!'})

# @app.route('/api/speedtest')
# def get_speed():
#   return jsonify(latest_speed)

# @app.route('/api/books')
# def get_books():
#   return jsonify(scrape_books())





if __name__ == '__main__':
    print("[Flask] Starting server...")
    # Thread(target=update_speed, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
