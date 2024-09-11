from flask import Flask, Response, request
from ptyprocess import PtyProcess
import os
import select

app = Flask(__name__)

# Initialize a PTY (Pseudo-Terminal)
process = PtyProcess.spawn(['/bin/bash'])

@app.route('/')
def index():
    return 'Web-Based Terminal is Running! Access the /shell endpoint to use it.'

@app.route('/shell', methods=['GET', 'POST'])
def shell():
    if request.method == 'POST':
        # Read user input and send it to the PTY
        command = request.form.get('command') + '\n'
        process.write(command.encode())

    # Read the output from the PTY
    output = b""
    while process.isalive():
        r, _, _ = select.select([process.fd], [], [], 0)
        if process.fd in r:
            output += process.read()

    return Response(output.decode(), mimetype='text/plain')

if __name__ == '__main__':
    # Run the app
    port = int(os.environ.get("PORT", 8080))  # Koyeb uses PORT environment variable
    app.run(host='0.0.0.0', port=port)
