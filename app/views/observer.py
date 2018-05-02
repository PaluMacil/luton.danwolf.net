from flask import jsonify, Blueprint, current_app, request, abort
from app.db import Db


observer = Blueprint('profile', __name__, url_prefix='observation')

@observer.route('/')
def home():
    return 'Hello World!'

@observer.route('/list', methods=['GET'])
def list_observations():
    db = Db.instance(current_app)
    obs = db.observations.all()
    return jsonify(obs)

@observer.route('/<id>')
def observation(id):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    else: return abort(400)
