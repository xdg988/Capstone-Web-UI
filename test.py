"""Filename: hello-world.py
  """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world(username='World'):

    return("Hello {}!".format(username))

app.run(host = '0.0.0.0' ,port = 80)