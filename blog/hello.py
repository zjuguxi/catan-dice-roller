from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
import views

app = Flask(__name__)
manager = Manager(app)
boostrap = Bootstrap(app)
moment = Moment(app)

if __name__ == '__main__':
    manager.run(debug = True)