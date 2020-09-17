from flask import request as r
from flask_restful import Resource
import requests as req
from requests.auth import HTTPBasicAuth
user = 'SK20841af8008834611f84e7590630f467'
pwd = 'oRob0tiWhYPm9gLQChE9FxX1vViOsI2U'


def cfr(b):
    d = b
    a = {}
    a["id"] = d["sid"]
    a["roomUniqueName"] = d["unique_name"]
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


class CompleteRoom(Resource):
    def get(self, uniqueName):
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "Status": "completed"
        }
        call = req.post("https://video.twilio.com/v1/Rooms/" + uniqueName,
                        data=payload, headers=head, auth=HTTPBasicAuth(user, pwd))
        # print(call.json())
        if call.status_code >= 400:
            if call.status_code == 404:
                return {"message": "Room not Found"}, 404

            x = cfr(call.json())

        return x, 202
