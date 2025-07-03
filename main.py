import os
from rotas import app
from flask_wtf.csrf import CSRFProtect


if __name__ == "__main__":
    debug = True
    ip = "127.0.0.1"
    port = int(os.getenv('PORT', '5000'))
    
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    
    app.run(ip, port, debug=debug)
    
    