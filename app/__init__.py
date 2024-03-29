from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.debug=True

    app.secret_key="monishbolimaga"
    app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024
    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.upload import bp as upload_bp
    app.register_blueprint(upload_bp,url_prefix='/upload')

    from app.inspection import bp as inspection_bp
    app.register_blueprint(inspection_bp,url_prefix='/inspection')

    from app.videos import bp as videos_bp
    app.register_blueprint(videos_bp,url_prefix='/videos')

    @app.route('/test/')
    def test_page():
        print("Hello")
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
