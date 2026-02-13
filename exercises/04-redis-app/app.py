from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis using container name as hostname
redis_host = os.environ.get('REDIS_HOST', 'redis-db')
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def home():
    # Increment visit counter
    visits = redis_client.incr('visits')
    return jsonify({
        'message': 'Hello from Flask!',
        'visits': visits
    })

@app.route('/reset')
def reset():
    redis_client.set('visits', 0)
    return jsonify({'message': 'Counter reset!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
