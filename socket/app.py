import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'abc'
app.config['DEBUG'] = True


app.static_folder = os.path.join(os.path.dirname(__file__), 'static')


@app.route('/')
def index_view():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    print('msg:', msg)
    return send(msg, broadcast=True)


if __name__ == '__main__':

    socketio.run(app)
