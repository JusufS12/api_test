from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

load_dotenv()
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')



################# ROUTING #################

# @app.route('/api/data', methods=['GET'])
# def get_data():
#   return jsonify({'message': 'Hello from Flask!'})




if __name__ == '__main__':
    print("[Flask] Starting server...")
    # Thread(target=update_speed, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
