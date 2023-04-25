from flask import Flask, Response, render_template
from flask_restful import Api, Resource
from resources.Decks import MetaDecks
from resources.Events import LastEvents

from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

#App instance

app= Flask(__name__)
api = Api(app)

class Default(Resource):
    def get(self):
        return Response(render_template('index.html'), mimetype='text/html')

#Add resources 
api.add_resource(MetaDecks,'/metadecks')
api.add_resource(LastEvents,'/last-events')
api.add_resource(Default,'/')

#Handle errors
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    
    abort(400, error=str(err))

if __name__ == '__main__':
    app.run()