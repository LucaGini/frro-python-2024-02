"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona

conexion = sqlite3.connect('soporte_practica_4.db')
def buscar_persona(id_persona):
    cursor = conexion.cursor()
    select = "SELECT * FROM Persona WHERE IdPersona = ?"
    cursor.execute(select, (id_persona,))
    resultado = cursor.fetchone()
    if resultado:
        conexion.commit()
        return resultado
    else:
        return False
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(1)
    assert juan == (1, 'juan perez', '1988-05-15 00:00:00', 32165498, 180)
    assert buscar_persona(12345) is False
#agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
#datetime.datetime(1988, 5, 15)
if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
