import os
from rotas import app


if __name__ == "__main__":
    debug = True
    ip = "127.0.0.1"
    port = int(os.getenv('PORT', '5000'))
    
    app.run(ip, port, debug=debug)
    
    