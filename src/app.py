from flask import Flask, request, jsonify

# Init app
app = Flask(__name__)

from src.controllers import index, user