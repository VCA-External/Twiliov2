from flask import request as r
from flask_restful import Resource
import requests as req
from requests.auth import HTTPBasicAuth
from util import get_random_string

user = 'SK20841af8008834611f84e7590630f467'
pwd = 'oRob0tiWhYPm9gLQChE9FxX1vViOsI2U'


def create_transform(b):
    d = b
    a = {}
    a["id"] = d["sid"]
    a["roomUniqueName"] = d["unique_name"]
    a["roomSID"] = None
    a["rooomstatus"] = d["status"]
    a["maxparticipants"] = d["max_participants"]
    a["type"] = d["type"]
    a["startAt"] = None
    a["endDt"] = None
    a["duration"] = 0
    a["createdDt"] = d["date_created"]
    a["modifiedDt"] = d["date_updated"]
    a["participants"] = []
    return a


class CreateRoom(Resource):
    def post(self):
        request = r.get_json()
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "MaxParticipants": 4,
            "Type": "group-small"
        }
        if request is not None:  # dict type
            if (request['roomUniqueName'] is not None):
                payload["UniqueName"] = str(request['roomUniqueName']) + \
                    get_random_string(4)

            if (request['maxParticipants']):
                if (request['maxParticipants'] > 4):
                    payload["Type"] = "group"

                payload['MaxParticipants'] = request['maxParticipants']
            if (request['RecordParticipantConnect'] is not None):
                payload["RecordParticipantsOnConnect"] = request["RecordParticipantConnect"]
            else:
                return {"message": "Bad request please retry"}, 400

            call = req.post('https://video.twilio.com/v1/Rooms/', auth=HTTPBasicAuth(
                user, pwd), headers=head, data=payload)
            return call.json(), 201
            if call.status_code == 400:
                if call.json()['code'] == 53113:
                    return {'message': "Room already exists"}, 400
        return {'message': "Room name is invalid"}, 400
