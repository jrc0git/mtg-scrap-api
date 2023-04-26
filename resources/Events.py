from logic.EventsLogic import getLastEvents, getLastEventsFormat
from flask_restful import Resource

class LastEvents(Resource):
    def get(self):
        return getLastEvents()
class LastEventsFormat(Resource):
    def get(self, format):
        return getLastEventsFormat(format)