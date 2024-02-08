from flask import Flask
from src.routes import bp as main_bp
from src.database import create_database
import logging

def create_app():
    app = Flask(__name__)

    logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    app.register_blueprint(main_bp)

    # Call create_database function within the application context
    with app.app_context():
        create_database()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
