import os

basedir= os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "GDtfDCFYjD"
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'datos.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False