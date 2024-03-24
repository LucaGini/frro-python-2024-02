"""Slicing."""

"""Toma un string y devuelve un booleano en base a si se lee igual al
derecho y al revés.

Restricción: No utilizar bucles - Usar Slices de listas.
Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
"""
def es_palindromo(palabra: str) -> bool:
    if palabra == palabra[::-1]:
        return True
    else:
        return False


    pass # Completar


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################
"""Toma un string y devuelve la mitad. Si la longitud es impar, redondear
hacia arriba.

Restricción: No utilizar bucles - Usar Slices de listas.
Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
"""

def mitad(palabra: str) -> str:
    if len(palabra) % 2 != 0:
        mitadp = (len(palabra) // 2 + 1)
    else:
        mitadp = len(palabra) // 2
    return palabra[:mitadp]
    pass # Completar


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
