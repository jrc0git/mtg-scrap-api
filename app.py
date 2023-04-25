from flask import Flask
from flask_restful import Api
from resources.Decks import MetaDecks
from resources.Events import LastEvents

#App instance

app= Flask(__name__)
api = Api(app)

#Add resources 

api.add_resource(MetaDecks,'/metadecks/<string:meta>')
api.add_resource(LastEvents,'/last-events')

if __name__ == '__main__':
    app.run()