from flask import Flask, jsonify
import socket
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Dockerized Python API!',
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().isoformat(),
        'version': os.environ.get('APP_VERSION', '1.0.0')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/info')
def info():
    return jsonify({
        'python_version': os.sys.version,
        'hostname': socket.gethostname(),
        'environment': {k: v for k, v in os.environ.items() if not k.startswith('_')}
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
