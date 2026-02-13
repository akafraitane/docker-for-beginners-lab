from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
import time

app = Flask(__name__)
CORS(app)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB_HOST', 'todo-db'),
                database=os.environ.get('DB_NAME', 'todos'),
                user=os.environ.get('DB_USER', 'postgres'),
                password=os.environ.get('DB_PASSWORD', 'postgres')
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("Could not connect to database")

@app.route('/api/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, completed, created_at FROM todos ORDER BY created_at DESC')
    todos = [{'id': row[0], 'title': row[1], 'completed': row[2], 'created_at': str(row[3])} 
             for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO todos (title) VALUES (%s) RETURNING id', (data['title'],))
    todo_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': todo_id, 'title': data['title'], 'completed': False}), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE todos SET completed = %s WHERE id = %s', (data['completed'], todo_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todos WHERE id = %s', (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
