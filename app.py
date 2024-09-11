# app.py
from flask import Flask
from flask_shell2http import Shell2HTTP
import os

app = Flask(__name__)

# Create the Shell2HTTP object
shell2http = Shell2HTTP(app=app, base_url_prefix="/", commands={
    'shell': '/bin/bash'  # Specify the shell you want to use, here we use bash
})

# Define a simple route to ensure the app is running
@app.route('/')
def index():
    return 'Web-Based Terminal is Running! Access the /shell endpoint to use it.'

if __name__ == '__main__':
    # Run the app
    port = int(os.environ.get("PORT", 8080))  # Koyeb uses PORT environment variable
    app.run(host='0.0.0.0', port=port)
