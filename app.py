from flask import Flask
import os
from bp_product import product
from models import db
#base directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.register_blueprint(product, url_prefix="/api")

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)




if __name__ == '__main__':
    app.run(debug=True)
