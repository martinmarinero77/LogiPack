from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)

class paquete(db.Model):
    __tablename__='paquete'
    id=db.Column(db.Integer, primary_key=True)
    numeroEnvio=db.Column(db.String(50))
    peso=db.Column(db.Integer)
    nomDestinatario=db.Column(db.String(50))
    dirDestinatario=db.Column(db.String(50))
    entregado=db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.Text, default='')
    idSucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idTransporte=db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idRepartidor=db.Column(db.Integer, db.ForeignKey('repartidor.id'),default=0)

class repartidor(db.Model):
    __tablename__='repartidor'
    id=db.Column(db.Integer, primary_key=True, default=0)
    numero=db.Column(db.Integer)
    nombre=db.Column(db.String(50))
    dni=db.Column(db.String(50), unique=True)
    idSucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes=db.relationship('paquete', backref='repartidor', cascade='all,delete-orphan')



class sucursal(db.Model):
    __tablename__='sucursal'
    id=db.Column(db.Integer, primary_key=True, default=0)
    numero=db.Column(db.Integer, unique=True)
    provincia=db.Column(db.String(50))
    localidad=db.Column(db.String(50))
    direccion=db.Column(db.String(50), unique=True)
    paquetes=db.relationship('paquete', backref='sucursal', cascade='all,delete-orphan')
    transportes=db.relationship('transporte', backref='sucursal', cascade='all,delete-orphan')
    repartidores=db.relationship('repartidor', backref='sucursal', cascade='all,delete-orphan')

class transporte(db.Model):
    __tablename__='transporte'
    id=db.Column(db.Integer, primary_key=True)
    numeroTransporte=db.Column(db.Integer)
    fechaHoraSalida=db.Column(db.DateTime)
    fechaHoraLlegada=db.Column(db.DateTime)
    idSucursal=db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes=db.relationship('paquete', backref='transporte', cascade='all,delete-orphan')






