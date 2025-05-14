from flask import Flask
from flask_migrate import Migrate

from server.models import db  # This assumes models.py is inside the server folder
from server.models import Pet  # Same here

# create a Flask application instance
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to the Pet API!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
