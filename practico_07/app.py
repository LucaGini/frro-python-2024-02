import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Agregar la ruta de practico_06 al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'practico_06')))

from capa_negocio import NegocioSocio, DniRepetido, LongitudInvalida, MaximoAlcanzado
from practico_05.ejercicio_01 import Socio

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

# Crear una instancia de NegocioSocio
negocio = NegocioSocio()

@app.route('/')
def index():
    # Obtener todos los socios
    socios = negocio.todos()
    return render_template('socios.html', socios=socios)

# Ruta para Alta de Socios
@app.route('/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        
        socio = Socio(nombre=nombre, apellido=apellido, dni=dni)
        
        try:
            negocio.alta(socio)
            flash('Socio dado de alta con éxito', 'success')
            return redirect(url_for('index'))
        except DniRepetido:
            flash('Error: El DNI ya está registrado', 'danger')
        except LongitudInvalida:
            flash('Error: El nombre o apellido tiene una longitud inválida', 'danger')
        except MaximoAlcanzado:
            flash('Error: Se ha alcanzado el número máximo de socios', 'danger')
    
    return render_template('alta.html')

# Ruta para Baja de Socios
@app.route('/baja/<int:id>', methods=['POST'])
def baja(id):
    if negocio.baja(id):
        flash('Socio dado de baja con éxito', 'success')
    else:
        flash('Error: No se pudo dar de baja al socio', 'danger')
    return redirect(url_for('index'))

# Ruta para Modificar Socios
@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    socio = negocio.buscar(id)
    if request.method == 'POST':
        socio.nombre = request.form['nombre']
        socio.apellido = request.form['apellido']
        socio.dni = request.form['dni']
        
        try:
            negocio.modificacion(socio)
            flash('Socio modificado con éxito', 'success')
            return redirect(url_for('index'))
        except LongitudInvalida:
            flash('Error: El nombre o apellido tiene una longitud inválida', 'danger')
    
    return render_template('modificar.html', socio=socio)

if __name__ == '__main__':
    app.run(debug=True)
