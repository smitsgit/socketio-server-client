"""
https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
https://pypi.org/project/socketIO-client/

"""

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my_event', namespace='/test')
def test_message(message):
    print(message)
    emit('my_response', {'data': message['data']})


@socketio.on('my_broadcast_event', namespace='/test')
def test_message(message):
    emit('my_response', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, port=5002)
