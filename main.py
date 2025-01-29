import os
from scripts.env import EnvVariables
from scripts.rotas import *


if __name__ == "__main__":
    debug = False
    rota = "127.0.0.1"
    port = int(os.getenv('PORT', '5000'))

    if (EnvVariables.ambiente == 0):
        debug = True
    
    if (EnvVariables.ambiente == 1):
        rota = EnvVariables.rota_dev
    
    app.run(rota, port, debug=debug)
    
    