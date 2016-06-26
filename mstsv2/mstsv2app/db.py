from flask_sqlalchemy import SQLAlchemy

# DB File is kept apart from the main file. This instantiates all of the SQLAlchemy
# database functinality. This allows for db to be imported into the different modules.

db = SQLAlchemy()
