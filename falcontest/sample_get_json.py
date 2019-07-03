# sample.py
import falcon
import os
import socket


class RequestGetJson:
    def on_get(self, req, resp):
        quote = {
            'author': 'Grace Hopper',
            'hostname': socket.gethostname(),
            'virtualhost': os.environ['VIRTUAL_HOST'],
        }
        resp.media = quote


api = falcon.API()
api.add_route('/quote', RequestGetJson())
