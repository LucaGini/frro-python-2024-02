import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio

# Implementar los metodos de la capa de negocio de socios.


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        """
        # Regla 1: DNI único
        if not self.regla_1(socio):
            raise DniRepetido("El DNI ya está registrado.")

        # Regla 2: Longitud del nombre y apellido
        if not self.regla_2(socio):
            raise LongitudInvalida("El nombre o apellido tiene una longitud inválida.")

        # Regla 3: No superar la cantidad máxima de socios
        if not self.regla_3():
            raise MaximoAlcanzado("Se ha alcanzado el número máximo de socios.")

        # Si pasa todas las validaciones, se da de alta el socio
        return self.datos.alta(socio)

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        """
        socio = self.buscar(id_socio)
        if socio:
            return self.datos.baja(id_socio)
        return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        """
        if not self.regla_2(socio):
            raise LongitudInvalida()

        return self.datos.modificacion(socio)

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es único.
        """
        socio_existente = self.buscar_dni(socio.dni)
        if socio_existente and socio_existente.id_socio != socio.id_socio:
            return False
        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido tengan más de 3 caracteres y menos de 15.
        """
        if not (self.MIN_CARACTERES <= len(socio.nombre) <= self.MAX_CARACTERES):
            return False
        if not (self.MIN_CARACTERES <= len(socio.apellido) <= self.MAX_CARACTERES):
            return False
        return True

    def regla_3(self):
        """
        Validar que no se esté excediendo la cantidad máxima de socios.
        """
        if len(self.todos()) >= self.MAX_SOCIOS:
            return False
        return True

