from flask import Flask
import os
app = Flask(__name__, root_path=os.getcwd())

from server import routes
