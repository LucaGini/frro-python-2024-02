"""For-Else, Any."""

from typing import Iterable

"""Toma una lista y devuelve un booleano en función si tiene al menos un
número par."""

def tiene_pares_basico(numeros: Iterable[int]) -> bool:
    bandera = False
    for numero in numeros:
        if numero % 2 == 0:
            bandera = True
    return bandera

    pass # Completar


# NO MODIFICAR - INICIO
assert tiene_pares_basico([1, 3, 5]) is False
assert tiene_pares_basico([1, 3, 5, 6]) is True
assert tiene_pares_basico([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando for-else con dos return y un break.
Referencia: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
"""

def tiene_pares_for_else(numeros: Iterable[int]) -> bool:
    for numero in numeros:
        if numero % 2 == 0:
            return True
            break
    else:
        return False

    pass # Completar


# NO MODIFICAR - INICIO
assert tiene_pares_for_else([1, 3, 5]) is False
assert tiene_pares_for_else([1, 3, 5, 6]) is True
assert tiene_pares_for_else([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################

"""Re-Escribir utilizando la función any, sin utilizar bucles.
Referencia: https://docs.python.org/3/library/functions.html#any
"""
def tiene_pares_any(numeros: Iterable[int]) -> bool:
    return any(numero % 2 == 0 for numero in numeros)
    pass # Completar


# NO MODIFICAR - INICIO
assert tiene_pares_any([1, 3, 5]) is False
assert tiene_pares_any([1, 3, 5, 6]) is True
assert tiene_pares_any([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN
