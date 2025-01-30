import os
from scripts.env import EnvVariables
from scripts.rotas import *
from gevent.pywsgi import WSGIServer


if __name__ == "__main__":
    port = int(os.getenv('PORT', '5000'))
    if (EnvVariables.ambiente == 0):
        debug = False
        ip = "127.0.0.1"
        
        app.run(ip, port, debug=True)
    else:
        http_server = WSGIServer(('0.0.0.0', port), app)
        http_server.serve_forever()
    