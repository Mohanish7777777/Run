# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from ptyprocess import PtyProcess
import os
import select

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

# Initialize a PTY (Pseudo-Terminal)
process = PtyProcess.spawn(['/bin/bash'])

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('command')
def handle_command(data):
    command = data['command'] + '\n'
    process.write(command.encode())
    
    # Read the output from the PTY
    output = b""
    while process.isalive():
        r, _, _ = select.select([process.fd], [], [], 0)
        if process.fd in r:
            output += process.read()
    
    emit('response', {'output': output.decode()})

if __name__ == '__main__':
    # Run the app using the WSGI server specified in Procfile
    pass
