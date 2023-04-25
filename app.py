from flask import Flask, Response, render_template
from flask_restful import Api, Resource
from resources.Decks import MetaDecks
from resources.Events import LastEvents

#App instance

app= Flask(__name__)
api = Api(app)

#Add resources 

class Default(Resource):
    def get(self):
        return Response(render_template('index.html'), mimetype='text/html')

api.add_resource(MetaDecks,'/metadecks/<string:meta>')
api.add_resource(LastEvents,'/last-events')
api.add_resource(Default,'/')

if __name__ == '__main__':
    app.run()