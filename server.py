from flask import Flask
from flask import request
import jwt
from dotenv import dotenv_values
config = dotenv_values('.env')
app = Flask(__name__)

def _authMiddleware(token):
  public_key = config['SERVICE_PUBLIC_KEY']
  public_key = public_key.replace('\\n', '\n')
  decoded = jwt.decode(token, public_key, audience='home-command-center', algorithms=['RS256'])
  return

@app.route('/', methods = ['POST'])
def command():
  token = request.headers.get('auth')
  _authMiddleware(token)
  return "Hello World!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
