from logic.EventsLogic import getLastEvents
from flask_restful import Resource

class LastEvents(Resource):
    def get(self):
        return getLastEvents()