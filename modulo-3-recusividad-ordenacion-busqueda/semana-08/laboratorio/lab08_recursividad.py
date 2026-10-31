"""
Lab 8 - Recursividad (con uso de IA)
INF 222 Estructura de Datos . Semestre 2026-2

===================================
DECLARACIÓN DE USO DE IA
===================================
Herramienta usada : ChatGPT
Para qué se usó : Para guiarme en la implementación de las funciones recursivasy obtener el trazado paso a paso de fibonacci(5).
Qué hice yo : Cpmprendí la logica de los algoritmos, adapté el código a mi entorno.
puedo explicar  : si
"""

import time
from functools import lru_cache

# =============================================================================
# PARTE 1 — FACTORIAL
# =============================================================================

def factorial(n):
    """
    Calcula n! de forma recursiva.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n × factorial(n-1)
    Complejidad: O(n) tiempo, O(n) espacio (por la pila de llamadas).
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# =============================================================================
# PARTE 2 — FIBONACCI
# =============================================================================

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci recursivamente.
    Esta implementación es ineficiente: O(2^n) llamadas.
    Solo para propósitos de análisis y trazado.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memoizado(n):
    """
    Calcula el n-ésimo número de Fibonacci con memoización.
    O(n) tiempo, O(n) espacio.
    """
    if n <= 1:
        return n
    return fibonacci_memoizado(n - 1) + fibonacci_memoizado(n - 2)


def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci iterativamente.
    O(n) tiempo, O(1) espacio.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# =============================================================================
# PARTE 3 — TORRES DE HANOI
# =============================================================================

movimientos = []  # lista global para registrar los movimientos

def torres_de_hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de Torres de Hanoi para n discos.
    Parámetros:
        n:         número de discos a mover
        origen:    poste donde están los n discos al inicio
        destino:   poste al que deben llegar todos los discos
        auxiliar:  poste auxiliar
    Efecto: agrega strings a `movimientos` con cada movimiento.
    Complejidad: O(2^n - 1) movimientos.
    """
    if n == 1:
        movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # 1. Mover n-1 discos de origen a auxiliar (usando destino como aux)
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    
    # 2. Mover el disco n (el más grande) de origen a destino
    movimientos.append(f"Mover disco {n} de {origen} a {destino}")
    
    # 3. Mover n-1 discos de auxiliar a destino (usando origen como aux)
    torres_de_hanoi(n - 1, auxiliar, destino, origen)

    """
    ============================
    TRAZADO PROPIO
    ============================
    La función comienza llamando a fib(5) ,la cual se divide en fib(4) y fib(3) .
    A su vez fib(4) se divide en fib(3) y fib(2) ,creando múltiples llamadas repetidas
    (por ejemplo, fib(3) se calcula varias veces de forma redundante). 
    Este árbol de llamadas continúa ramificándose hacia abajo hasta llegar a los casos base (fib(1) o fib(0)
    que devuelven 1 o 0 respectivamente), cuyos resultados empiezan a retornar hacia arriba para sumar los valores finales.
    """

    """
    ========================================
     Diagrama ASCII de la pila de llamadas
    ========================================
    fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) -> 1
│   │   │   └── fib(0) -> 0
│   │   └── fib(1) -> 1
│   └── fib(2)
│       ├── fib(1) -> 1
│       └── fib(0) -> 0
└── fib(3)
    ├── fib(2)
    │   ├── fib(1) -> 1
    │   └── fib(0) -> 0
    └── fib(1) -> 1
    """