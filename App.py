from datetime import datetime
from flask import Flask, request, render_template,session
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')

from Models import db
from Models import paquete, repartidor, sucursal,transporte

@app.route('/')
def Inicio():    
    return render_template('Inicio.html',paquetes=paquete.query.all(), repartidores=repartidor.query.all(),
    sucursales=sucursal.query.all(), transportes=transporte.query.all())

@app.route('/Elegir_Sucursal', methods=['GET', 'POST'])
def Elegir_Sucursal():
    if request.method == 'POST':
        sucursal_id = request.form.get('sucursales')
        session['idSucursal']=sucursal_id
        if not sucursal_id:
            return render_template('Error.html', error="Por favor, Seleccione una sucursal.")
        # Obtener la sucursal seleccionada por su ID
        else:
            sucursal_actual = sucursal.query.get(sucursal_id)   
            return render_template('Funcionalidades.html', sucursal=sucursal_actual)
        
    else:
        sucursales = sucursal.query.order_by(sucursal.numero).all()
        return render_template('ElegirSucursal.html', sucursales=sucursales)
    
@app.route('/Registrar_Paquete/<int:sucursal_id>', methods=['GET', 'POST'])
def Registrar_Paquete(sucursal_id):
    sucursal_actual = sucursal.query.get(sucursal_id)
    if request.method=='POST':
        if not request.form['peso'] or not request.form['nombre'] or not request.form['direccion']:
            return render_template('Error.html', error="Por favor, Ingrese todos los datos solicitados.")
        else:
            numero_random = random.randint(0, 2000)
            sucu=sucursal_actual
            nuevo_paquete=paquete(numeroEnvio=numero_random, peso=request.form['peso'], nomDestinatario=request.form['nombre'],
            dirDestinatario=request.form['direccion'], idSucursal=sucu.id)
            db.session.add(nuevo_paquete)
            db.session.commit()
            return render_template('RegistroExitoso.html',paquete=nuevo_paquete, sucursal=sucursal_actual)
    else:
        return render_template('RegistrarPaquete.html', sucursal=sucursal_actual)
    
@app.route('/Volver_Funcio/<int:sucursal_id>', methods=['GET', 'POST'])
def Volver_Funcio(sucursal_id):
    sucursal_actual = sucursal.query.get(sucursal_id)
    return render_template('Funcionalidades.html', sucursal=sucursal_actual)


@app.route('/Elegir_Sucursal_Transporte', methods=['GET', 'POST'])
def Elegir_Sucursal_Transporte():
    if request.method == 'POST':
        sucursal_id = request.form.get('sucursales')
        if not sucursal_id:
            return render_template('Error.html', error="Por favor, Seleccione una sucursal.")
        # Obtener la sucursal seleccionada por su ID
        else:
            sucursal_actual = sucursal.query.get(sucursal_id)
            sucursal_vieja=session['idSucursal']
            paquete_no_entregado= paquete.query.filter_by(entregado=False, idRepartidor=0,idSucursal=sucursal_vieja).all()  
            if not paquete_no_entregado:
                 return render_template('Error.html', error="No hay Paquetes sin entregar.")
            else:
                return render_template('Paq_no_Entregados.html', sucursal=sucursal_actual,paquetes=paquete_no_entregado)
        
    else:
        sucursales = sucursal.query.order_by(sucursal.numero).all()
        return render_template('Sucursal_Transporte.html', sucursales=sucursales)

@app.route('/Transporte_Registrado/<int:sucursal_id>', methods=['GET', 'POST'])
def Transporte_Registrado(sucursal_id):
    sucursal_actual = sucursal.query.get(sucursal_id)
    sucu=sucursal_actual
    if request.method == 'POST':
        paquete_seleccionados = request.form.getlist('paquetes_seleccionados[]')
        if not paquete_seleccionados:
            return render_template('Error.html', error="Por favor, Seleccione al menos un Paquete.")
        else:  
            nroTrans=random.randint(0, 2000)
            fechas=datetime.now()
            fechal=None
            idSucu=sucu.id
            nuevo_transporte=transporte(numeroTransporte=nroTrans, fechaHoraSalida=fechas,
            fechaHoraLlegada=fechal, idSucursal=idSucu)
            paquetes=[]
            for paquete_id in paquete_seleccionados:
                paquete_actual = paquete.query.get(paquete_id)
                paquete_actual.idSucursal=sucu.id
                db.session.add(paquete_actual)
                db.session.commit()
                paquetes.append(paquete_actual)
                nuevo_transporte.paquetes.append(paquete_actual)
            db.session.add(nuevo_transporte)
            db.session.commit()
            return render_template('TransporteRegistrado.html',paquetes=paquetes,transporte=nuevo_transporte)
        
@app.route('/Llegada_Registrada/<int:sucursal_id>', methods=['GET', 'POST'])
def Llegada_Registrada(sucursal_id):
    sucursal_actual = sucursal.query.get(sucursal_id)
    sucu=sucursal_actual
    if request.method == 'POST':
        transporte_seleccionados = request.form.getlist('trans_seleccionados[]')
        if not transporte_seleccionados:
            return render_template('Error.html', error="Por favor, Seleccione al menos un transporte de la lista.")
        else:  
            transportes=[]
            for transporte_id in transporte_seleccionados:
                transporte_actual=transporte.query.get(transporte_id)
                fechal=datetime.now()
                transporte_actual.fechaHoraLlegada=fechal
                transportes.append(transporte_actual)
                db.session.commit()
            return render_template('LlegadaRegistrada.html',transportes=transportes,sucursal=sucursal_actual)
    else:
        transportes = transporte.query.filter_by(fechaHoraLlegada=None, idSucursal=sucu.id).all()
        if not transportes:
            return render_template('Error2.html', error="No hay Transportes con destino a la Sucursal.")
        else:
            return render_template('Trans_no_llegado.html', transportes=transportes,sucursal=sucursal_actual)

if __name__ == '__main__':
    app.run(debug = True)



