from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os

# Añadimos la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora importamos los módulos
from practico_06.capa_negocio import NegocioSocio, DniRepetido, LongitudInvalida, MaximoAlcanzado
from practico_05.ejercicio_01 import Socio


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Para habilitar los mensajes flash

# Inicializamos la capa de negocio
negocio_socio = NegocioSocio()

@app.route('/')
def index():
    socios = negocio_socio.todos()  # Obtener la lista de todos los socios
    return render_template('socios.html', socios=socios)

@app.route('/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']

        # Crear una instancia de socio
        nuevo_socio = Socio(dni=dni, nombre=nombre, apellido=apellido)

        try:
            negocio_socio.alta(nuevo_socio)
            flash('Socio agregado exitosamente!', 'success')
            return redirect(url_for('index'))
        except (DniRepetido, LongitudInvalida, MaximoAlcanzado) as e:
            flash(str(e), 'danger')

    return render_template('formulario.html', accion="Alta", socio=None)

@app.route('/baja/<int:id>')
def baja(id):
    if negocio_socio.baja(id):
        flash('Socio eliminado exitosamente!', 'success')
    else:
        flash('No se encontró el socio a eliminar.', 'danger')
    return redirect(url_for('index'))

@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    socio = negocio_socio.buscar(id)
    if not socio:
        flash('Socio no encontrado.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']

        socio.nombre = nombre
        socio.apellido = apellido
        socio.dni = dni

        try:
            negocio_socio.modificacion(socio)
            flash('Socio modificado exitosamente!', 'success')
            return redirect(url_for('index'))
        except LongitudInvalida as e:
            flash(str(e), 'danger')

    return render_template('formulario.html', accion="Modificar", socio=socio)

if __name__ == '__main__':
    app.run(debug=True)
