"""Propiedades"""

class Auto:
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    # Completar
    def __init__(self, marca: str, precio: float) -> None:
        self._marca = marca
        self._precio = precio

    @property #getters
    def marca(self) -> str:
        return self._marca.capitalize()
    @property #getters
    def precio(self) -> float:
        return round(self._precio, 2)
    @precio.setter
    def precio(self, value: float) -> None:
        self._precio = value
    @marca.setter
    def marca(self, value: str) -> None:
        self._marca = value
        raise AttributeError("La propiedad 'marca' no puede ser modificada") #preguntar

# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.marca == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.marca = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    """Re-Escribir utilizando DataClasses"""

    # Completar
    _marca: str
    _precio: float

    @property #getters
    def marca(self) -> str:
        return self._marca.capitalize()
    @property #getters
    def precio(self) -> float:
        return round(self._precio, 2)
    @precio.setter
    def precio(self, value: float) -> None:
        self._precio = value
    @marca.setter
    def marca(self, value: str) -> None:
        self._marca = value
        raise AttributeError("La propiedad 'marca' no puede ser modificada") #preguntar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.marca == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.marca = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
