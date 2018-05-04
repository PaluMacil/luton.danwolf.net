from flask import jsonify, Blueprint, current_app, request, abort
from app.db import Db
from datetime import datetime
import ifcfg


observer = Blueprint('profile', __name__, url_prefix='/observation')

@observer.route('/')
def home():
    return 'Hello World!'

@observer.route('/list', methods=['GET'])
def list_observations():
    db = Db.instance(current_app)
    obs = db.observations.all()
    return jsonify(obs)

@observer.route('/<int:id>')
def observation(id: int):
    db = Db.instance(current_app)
    if request.method == 'GET':
        obs = db.observations.one(id)
        if obs is None:
            return abort(404)
        return jsonify(obs)
    if request.method == 'POST':
        new_obs = request.get_json()
        obs = db.observations.add(new_obs.mac, new_obs.ipv4, new_obs.observation_type, datetime.now())
        if obs is None:
            return abort(500)
        return jsonify(obs)
    return abort(400)

@observer.route('/self', methods=['POST'])
def observe_self():
    interface = ifcfg.default_interface()
    db = Db.instance(current_app)
    obs = db.observations.add(interface.ether, interface.ipv4, interface.observation_type,  datetime.now())
    if obs is None:
        return abort(500)
    return jsonify(obs)