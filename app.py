from flask import Flask, request
from flask_restful import Api
from CreateRoom import CreateRoom
from CompleteRoom import CompleteRoom
from DeleteRoom import DeleteRoom

app = Flask(__name__)
api = Api(app)

api.add_resource(CreateRoom, '/api/rooms/createRoom')
api.add_resource(CompleteRoom, '/api/rooms/completeRoom/<string:uniqueName>')
api.add_resource(DeleteRoom, '/api/rooms/deleteRoom/<string:uniqueName>')
