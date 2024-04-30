"""Base de Datos SQL - Modificación"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_04 import buscar_persona

conexion = sqlite3.connect('soporte_practica_4.db')

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    cursor = conexion.cursor()
    select = "SELECT IdPersona FROM Persona WHERE IdPersona = ?"
    cursor.execute(select, (id_persona,))
    resultado = cursor.fetchone()
    if resultado:
        update = "UPDATE Persona SET Nombre=?, FechaNacimiento=?, DNI=?, Altura=? WHERE IdPersona = ?"
        data = (nombre, nacimiento, dni, altura, id_persona)
        cursor.execute(update, data)
        conexion.commit()
        return True
    else:
        return False
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""
    pass # Completar

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    #assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

#Por qué en el assert aparece que el id es 1. Cuando agrego a la persona, si es autoincremental, nunca va a ser 1.

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
