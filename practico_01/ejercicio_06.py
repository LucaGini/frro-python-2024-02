"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union

"""Toma una lista de enteros y strings y devuelve una lista con todos los
elementos numéricos al final.
"""
def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    numeros = []
    letras = []
    for elemento in lista:
        if isinstance(elemento, (int, float)):
            numeros.append(elemento)
        else:
            letras.append(elemento)
    return letras + numeros


    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################
"""Re-escribir utilizando comprensión de listas."""

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    numeros: List[float] = [elemento for elemento in lista if isinstance(elemento, (int, float))]
    letras:  List[str] = [elemento for elemento in lista if isinstance(elemento, str)]
    return letras + numeros
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################
"""Re-escribir utilizando la función sorted con una custom key.
Referencia: https://docs.python.org/3/library/functions.html#sorted
"""

def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    return sorted(lista, key=lambda x: isinstance(x, (int, float)))
    pass # Completar

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################
"""CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
Referencia: https://docs.python.org/3/library/functions.html#filter
"""

def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    letras = list(filter(lambda x: isinstance(x, str), lista))
    numeros = list(filter(lambda x: isinstance(x, (int, float)), lista))
    return letras + numeros
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""

#def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:

#    pass # Completar


# NO MODIFICAR - INICIO
#if __name__ == "__main__":
#    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
