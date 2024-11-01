from flask import Flask
from flask_cors import CORS
from .config import Config
from .models import db
from .middleware.error_handlers import register_error_handlers
from .utils.logging_config import setup_logging
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    
    setup_logging(app)
    register_error_handlers(app)
    
    from .routes import main_bp
    from .routes.contact_routes import contact_bp
    from .routes.media_routes import media_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(media_bp)
    
    os.makedirs(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']), exist_ok=True)

    with app.app_context():
        db.create_all()
    
    return app