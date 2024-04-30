"""Base de datos SQL - Listar"""

import datetime
import sqlite3

from practico_04.ejercicio_04 import buscar_persona
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla
from practico_04.ejercicio_07 import agregar_peso

conexion = sqlite3.connect('soporte_practica_4.db')
def listar_pesos(id_persona):
    cursor = conexion.cursor()
    existe = buscar_persona(id_persona)
    if existe:
        query = "SELECT strftime('%Y-%m-%d', Fecha), Peso FROM PersonaPeso WHERE IdPersona=? AND Fecha <= ?"
        cursor.execute(query, (id_persona, datetime.date.today()))
        datos = cursor.fetchall()
        print(datos)
        return datos
    else:
        return False

    """Implementar la funcion listar_pesos, que devuelva el historial de pesos 
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
     mplementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente 
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """
    #return []


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
