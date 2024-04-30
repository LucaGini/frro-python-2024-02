"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

conexion = sqlite3.connect('soporte_practica_4.db')
def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    cursor = conexion.cursor()
    query = """CREATE TABLE IF NOT EXISTS persona(
                    IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre CHAR(30),
                    FechaNacimiento DATE,
                    DNI INTEGER,
                    Altura INTEGER
                );"""
    cursor.execute(query)
    conexion.commit()
    pass # Completar


def borrar_tabla():
    cursor = conexion.cursor()
    cursor.execute(
        """DROP TABLE IF EXISTS Persona""")
    conexion.commit()
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        #borrar_tabla()
    return func_wrapper
#crear_tabla()
# NO MODIFICAR - FIN