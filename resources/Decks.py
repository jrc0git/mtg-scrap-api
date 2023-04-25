from logic.DecksLogic import getDecksByMeta
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, parser, abort

class MetaDecks(Resource):
    args_meta = {'meta':fields.Str(validate=validate.OneOf(['standard','modern','pioneer']))}
    @use_args(args_meta, location='query') #querystring
    def get(self, args):
        return getDecksByMeta(args['meta'])

    
   