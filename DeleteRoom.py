from flask import request as r
from flask_restful import Resource
import requests as req
from requests.auth import HTTPBasicAuth
user = 'SK20841af8008834611f84e7590630f467'
pwd = 'oRob0tiWhYPm9gLQChE9FxX1vViOsI2U'


class DeleteRoom(Resource):
    def delete(self, uniqueName):
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "Status": "completed"
        }
        call = req.post("https://video.twilio.com/v1/Rooms/" + uniqueName,
                        data=payload, headers=head, auth=HTTPBasicAuth(user, pwd))
        # print(call.json())

        if call.status_code == 404:
            return {"message": "Room not Found"}, 404

        return None, 200
