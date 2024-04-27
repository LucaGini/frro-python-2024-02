"""FOR, Sum, Reduce."""
"""Devuelve la suma de los números de 1 a N.

Restricción: Utilizar un bucle for.
"""

def sumatoria_basico(n: int) -> int:
    suma = 0
    for i in range(n+1):
        suma+=i
    return suma
    pass # Completar


# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando la función sum y sin usar bucles.
Referencia: https://docs.python.org/3/library/functions.html#sum
"""

def sumatoria_sum(n: int) -> int:
    return sum(range(1, n+1))

    pass # Completar


# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce

"""CHALLENGE OPCIONAL: Re-escribir utilizando reduce.
Referencia: https://docs.python.org/3/library/functools.html#functools.reduce
"""

def sumatoria_reduce(n: int) -> int:
    suma = reduce(lambda x, y: x + y, range(1,n+1))
    return suma
#utilizamos range(1, n + 1) para generar una secuencia de números desde 1 hasta N
# (ambos inclusive), y luego aplicamos la función reduce para obtener la suma total.

    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_gauss(n: int) -> int:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando suma de Gauss.
    Referencia: https://es.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    """
    return n*(n+1)//2 #formula de la suma de gauss, buscada en internet
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_gauss(1) == 1
    assert sumatoria_gauss(100) == 5050
# NO MODIFICAR - FIN
