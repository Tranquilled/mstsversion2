from mstsv2app import app
from mstsv2app.db import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from settings import HOST,PORT,DEBUG
import sys
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)


migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
	manager.run()
