from logic.DecksLogic import getDecksByMeta
from flask_restful import Resource

class MetaDecks(Resource):
    def get(self,meta):
        return getDecksByMeta(meta)