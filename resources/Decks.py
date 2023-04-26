from logic.DecksLogic import getDecksByMeta
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, parser

#class MetaDecks(Resource):
 #   args_meta = {'format':fields.Str(validate=validate.OneOf(['standard','modern','pioneer']))}
  #  @use_args(args_meta, location='query')
   # def get(self, args):
    #    return getDecksByMeta(args['format'])

class Decks(Resource):
    def get(self):
        return {'hello' : 'world'}
    
class DecksMeta(Resource):
    def get(self, format):
        return getDecksByMeta(format)