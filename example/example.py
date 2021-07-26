import logging
import json
import os
from dlist_top import Client

logging.basicConfig(level=logging.INFO)

config = json.load(open(os.path.dirname(__file__) + '/config.json'))

dlist = Client(token=config['token'])
dlist.connect()

@dlist.on('rate')
def on_rate(data):
    print(data)
    
@dlist.on('vote')
def on_vote(data):
    print(data)