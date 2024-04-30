"""Base de Datos SQL - Creación de tablas auxiliares"""
import sqlite3

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla

conexion=sqlite3.connect('soporte_practica_4.db')
def crear_tabla_peso():
    cursor = conexion.cursor()
    query = """CREATE TABLE IF NOT EXISTS PersonaPeso(
                        IdPersona INTEGER,
                        Fecha DATE,
                        Peso INTEGER,
                        FOREIGN KEY (IdPersona) REFERENCES persona(IdPersona)
                    );"""
    cursor.execute(query)
    conexion.commit()
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    pass # Completar


def borrar_tabla_peso():
    cursor = conexion.cursor()
    cursor.execute(
        """DROP TABLE IF EXISTS PersonaPeso""")
    conexion.commit()
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
