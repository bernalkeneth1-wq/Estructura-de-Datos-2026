"""
Lab 10 — Búsqueda Secuencial y Binaria
INF 222 Estructura de Datos · Semestre 2026-2
"""

import time
import random


# =============================================================================
# PARTE 1: BÚSQUEDA SECUENCIAL
# =============================================================================

def busqueda_secuencial(arr, objetivo):
    """
    Busca `objetivo` en `arr` recorriendo elemento por elemento.
    Retorna el índice donde se encontró, o -1 si no está.
    No requiere que el arreglo esté ordenado.
    Complejidad: O(n).
    """
    for i, val in enumerate(arr):
        if val == objetivo:
            return i
    return -1


# =============================================================================
# PARTE 2: BÚSQUEDA BINARIA (ITERATIVA)
# =============================================================================

def busqueda_binaria_iterativa(arr, objetivo):
    """
    Busca `objetivo` en `arr` ORDENADO usando búsqueda binaria.
    Retorna el índice donde se encontró, o -1 si no está.
    PRECONDICIÓN: arr debe estar ordenado de menor a mayor.
    Complejidad: O(log n).
    """
    izquierda = 0
    derecha = len(arr) - 1
    
    while izquierda <= derecha:
        mid = (izquierda + derecha) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izquierda = mid + 1
        else:
            derecha = mid - 1
            
    return -1


# =============================================================================
# PARTE 3: BÚSQUEDA BINARIA (RECURSIVA)
# =============================================================================

def busqueda_binaria_recursiva(arr, objetivo, izquierda=None, derecha=None):
    """
    Versión recursiva de la búsqueda binaria.
    Retorna el índice donde se encontró, o -1 si no está.
    PRECONDICIÓN: arr debe estar ordenado.
    Complejidad: O(log n) tiempo, O(log n) espacio (pila de llamadas).
    """
    if izquierda is None:
        izquierda = 0
    if derecha is None:
        derecha = len(arr) - 1

    # Caso base: espacio de búsqueda vacío
    if izquierda > derecha:
        return -1

    mid = (izquierda + derecha) // 2

    if arr[mid] == objetivo:
        return mid
    elif arr[mid] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, mid + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, mid - 1)


# =============================================================================
# COMPARACIÓN DE EFICIENCIA
# =============================================================================

def comparar_busquedas(n=100_000, repeticiones=1000):
    """
    Compara el tiempo de búsqueda secuencial vs. binaria en un arreglo de n elementos.
    """
    arr = list(range(0, n * 2, 2))  # [0, 2, 4, 6, ..., 2*(n-1)]  — ordenado
    objetivos = [random.randint(0, n * 2) for _ in range(repeticiones)]

    # Búsqueda secuencial
    t0 = time.perf_counter()
    for obj in objetivos:
        busqueda_secuencial(arr, obj)
    t_secuencial = time.perf_counter() - t0

    # Búsqueda binaria iterativa
    t0 = time.perf_counter()
    for obj in objetivos:
        busqueda_binaria_iterativa(arr, obj)
    t_binaria = time.perf_counter() - t0

    print(f"\nComparación ({repeticiones:,} búsquedas en arreglo de {n:,} elementos):")
    print(f"  Secuencial: {t_secuencial:.4f} s")
    print(f"  Binaria:    {t_binaria:.4f} s")
    if t_binaria > 0:
        print(f"  Razón:      {t_secuencial / t_binaria:.1f}× más rápida la binaria")


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":
    arr_ordenado = [5, 10, 20, 30, 40, 50, 60, 70, 80]
    arr_no_ordenado = [30, 10, 50, 5, 80, 40, 20, 60, 70]

    print("=" * 55)
    print("Búsqueda Secuencial (arreglo no ordenado)")
    print("=" * 55)
    casos = [(30, 0), (80, 4), (40, 5), (99, -1)]
    for obj, esperado in casos:
        resultado = busqueda_secuencial(arr_no_ordenado, obj)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] buscar({obj}): índice={resultado} (esperado={esperado})")

    print("\n" + "=" * 55)
    print("Búsqueda Binaria Iterativa (arreglo ordenado)")
    print("=" * 55)
    casos_b = [(40, 4), (5, 0), (80, 8), (55, -1)]
    for obj, esperado in casos_b:
        resultado = busqueda_binaria_iterativa(arr_ordenado, obj)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] buscar({obj}): índice={resultado} (esperado={esperado})")

    print("\n" + "=" * 55)
    print("Búsqueda Binaria Recursiva (arreglo ordenado)")
    print("=" * 55)
    for obj, esperado in casos_b:
        resultado = busqueda_binaria_recursiva(arr_ordenado, obj)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f"  [{estado}] buscar({obj}): índice={resultado} (esperado={esperado})")

    print("\n" + "=" * 55)
    print("Verificación de consistencia entre métodos")
    print("=" * 55)
    arr_test = sorted(random.sample(range(1, 200), 50))
    for _ in range(20):
        obj = random.randint(1, 200)
        r_iter = busqueda_binaria_iterativa(arr_test, obj)
        r_rec = busqueda_binaria_recursiva(arr_test, obj)
        r_seq = busqueda_secuencial(arr_test, obj)
        # Verificar que o todos encontraron o todos no encontraron
        encontrado_iter = r_iter != -1
        encontrado_rec = r_rec != -1
        encontrado_seq = r_seq != -1
        if not (encontrado_iter == encontrado_rec == encontrado_seq):
            print(f"  INCONSISTENCIA en objetivo={obj}: iter={r_iter}, rec={r_rec}, seq={r_seq}")
    print("  Verificación completada")

    print("\n" + "=" * 55)
    print("Comparación de tiempos")
    print("=" * 55)
    comparar_busquedas(n=50_000, repeticiones=500)