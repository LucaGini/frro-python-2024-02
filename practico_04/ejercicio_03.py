"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona

conexion = sqlite3.connect('soporte_practica_4.db')

def borrar_persona(id_persona):
    cursor = conexion.cursor()
    print(id_persona)
    select = "SELECT IdPersona FROM Persona WHERE IdPersona = ?"
    cursor.execute(select, (id_persona,))
    resultado = cursor.fetchone()
    print(resultado)
    if resultado:
        query = "DELETE FROM Persona WHERE IdPersona = ?"
        cursor.execute(query, (id_persona,))
        conexion.commit()
        return True
    else:
        return False
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    pass # Completar

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
