import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	welcome_text = os.environ.get('WELCOME')
	return f'Hello {welcome_text}'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
