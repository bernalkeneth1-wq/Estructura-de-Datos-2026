"""
Lab 11 — Taller Integrador: Ordenación + Búsqueda + Recursión
INF 222 Estructura de Datos · Semestre 2026-2

Este taller integra los tres grandes temas del Módulo 3. Deberás:
  - Elegir el algoritmo de ordenación más adecuado según el contexto.
  - Aplicar búsqueda binaria sobre la colección ordenada.
  - Diseñar una solución recursiva para un sub-problema.
  - Justificar las complejidades en las celdas marcadas como [ANÁLISIS].
"""

import time
import random


# =============================================================================
# PARTE 1: AGENDA DE CONTACTOS (ordenación + búsqueda)
# =============================================================================

CONTACTOS_EJEMPLO = [
    {"nombre": "Carlos", "apellido": "Zúñiga",   "telefono": "6001-0001"},
    {"nombre": "María",  "apellido": "Alvarado",  "telefono": "6001-0002"},
    {"nombre": "Luis",   "apellido": "Morales",   "telefono": "6001-0003"},
    {"nombre": "Ana",    "apellido": "Batista",   "telefono": "6001-0004"},
    {"nombre": "Pedro",  "apellido": "Rodríguez", "telefono": "6001-0005"},
    {"nombre": "Sandra", "apellido": "López",     "telefono": "6001-0006"},
    {"nombre": "Jorge",  "apellido": "Chávez",    "telefono": "6001-0007"},
    {"nombre": "Elena",  "apellido": "Morales",   "telefono": "6001-0008"},
]


def ordenar_contactos(contactos):
    """
    [ANÁLISIS] ¿Por qué elegiste ese algoritmo?
    Se eligió Timsort (implementado de forma nativa en la función sorted() de Python), 
    ya que es un algoritmo híbrido sumamente eficiente con una complejidad de O(n log n) 
    en el peor y promedio caso. Además, es un algoritmo estable, lo cual es ideal para 
    ordenar diccionarios complejos permitiendo claves múltiples (por apellido y nombre).
    """
    return sorted(contactos, key=lambda c: (c['apellido'], c['nombre']))


def buscar_por_apellido(contactos_ordenados, apellido_buscado):
    """
    Busca TODOS los contactos cuyo 'apellido' == apellido_buscado.
    `contactos_ordenados` ya está ordenado por apellido.
    Retorna lista de contactos encontrados (puede ser más de uno).

    Estrategia sugerida:
      1. Usa búsqueda binaria para encontrar CUALQUIER coincidencia.
      2. Luego expande hacia la izquierda y la derecha para capturar todas.
    Complejidad esperada: O(log n + k) donde k = número de coincidencias.
    """
    izquierda = 0
    derecha = len(contactos_ordenados) - 1
    indice_encontrado = -1

    # Paso 1: Búsqueda binaria para localizar una coincidencia
    while izquierda <= derecha:
        mid = (izquierda + derecha) // 2
        if contactos_ordenados[mid]['apellido'] == apellido_buscado:
            indice_encontrado = mid
            break
        elif contactos_ordenados[mid]['apellido'] < apellido_buscado:
            izquierda = mid + 1
        else:
            derecha = mid - 1

    if indice_encontrado == -1:
        return []

    # Paso 2: Expandir lateralmente para capturar todas las coincidencias con el mismo apellido
    resultados = [contactos_ordenados[indice_encontrado]]
    
    # Expandir hacia la izquierda
    i = indice_encontrado - 1
    while i >= 0 and contactos_ordenados[i]['apellido'] == apellido_buscado:
        resultados.insert(0, contactos_ordenados[i])
        i -= 1

    # Expandir hacia la derecha
    j = indice_encontrado + 1
    while j < len(contactos_ordenados) and contactos_ordenados[j]['apellido'] == apellido_buscado:
        resultados.append(contactos_ordenados[j])
        j += 1

    return resultados


# =============================================================================
# PARTE 2: ESTADÍSTICAS RECURSIVAS
# =============================================================================

def suma_recursiva(nums):
    """Calcula la suma de `nums` usando recursión (sin usar sum())."""
    if not nums:
        return 0
    return nums[0] + suma_recursiva(nums[1:])


def maximo_recursivo(nums):
    """Encuentra el máximo de `nums` usando recursión (sin usar max())."""
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    sub_max = maximo_recursivo(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max


def cuenta_mayores_recursivo(nums, umbral, i=0):
    """Cuenta cuántos elementos de nums[i:] son estrictamente mayores que umbral."""
    if i >= len(nums):
        return 0
    actual = 1 if nums[i] > umbral else 0
    return actual + cuenta_mayores_recursivo(nums, umbral, i + 1)


# =============================================================================
# PARTE 3: POTENCIAS Y EXPONENCIACIÓN RÁPIDA
# =============================================================================

def potencia_lenta(base, exp):
    if exp == 0:
        return 1
    return base * potencia_lenta(base, exp - 1)


def potencia_rapida(base, exp):
    """Calcula base^exp con exponenciación por cuadrado O(log n)."""
    if exp == 0:
        return 1
    mitad = potencia_rapida(base, exp // 2)
    if exp % 2 == 0:
        return mitad * mitad
    else:
        return base * mitad * mitad


# =============================================================================
# PARTE 4: PROBLEMA INTEGRADOR — TOP-K PRODUCTOS
# =============================================================================

CATALOGO = [
    {"nombre": "Audífonos BT",     "precio": 45.99},
    {"nombre": "Cargador USB-C",   "precio": 12.50},
    {"nombre": "Funda celular",    "precio": 8.99},
    {"nombre": "Teclado inalám.",  "precio": 35.00},
    {"nombre": "Mouse ergonómico", "precio": 28.75},
    {"nombre": "Webcam HD",        "precio": 55.00},
    {"nombre": "Hub USB 4 puertos","precio": 18.00},
    {"nombre": "Soporte laptop",   "precio": 22.50},
    {"nombre": "Cable HDMI 2m",    "precio": 9.99},
    {"nombre": "Parlante portátil","precio": 39.00},
]


def top_k_baratos(catalogo, k):
    """Retorna los k productos más baratos del catálogo ordenados de menor a mayor precio."""
    catalogo_ordenado = sorted(catalogo, key=lambda p: p['precio'])
    return catalogo_ordenado[:k]


def rango_precio(catalogo_ordenado, precio_min, precio_max):
    """Retorna productos cuyo precio está en [precio_min, precio_max]."""
    return [p for p in catalogo_ordenado if precio_min <= p['precio'] <= precio_max]


# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

if __name__ == "__main__":

    # ---- PARTE 1 ----
    print("=" * 60)
    print("PARTE 1: Agenda de Contactos")
    print("=" * 60)

    ordenados = ordenar_contactos(CONTACTOS_EJEMPLO)
    if ordenados:
        print("Contactos ordenados:")
        for c in ordenados:
            print(f"  {c['apellido']:15} {c['nombre']:10} {c['telefono']}")

        encontrados = buscar_por_apellido(ordenados, "Morales")
        print(f"\nBúsqueda 'Morales': {len(encontrados) if encontrados else 0} resultado(s)")
        for c in (encontrados or []):
            print(f"  {c['nombre']} {c['apellido']} — {c['telefono']}")

        no_encontrado = buscar_por_apellido(ordenados, "García")
        print(f"Búsqueda 'García': {no_encontrado}")

    # ---- PARTE 2 ----
    print("\n" + "=" * 60)
    print("PARTE 2: Estadísticas Recursivas")
    print("=" * 60)
    nums = [4, 7, 2, 9, 1, 5]
    print(f"Lista: {nums}")
    print(f"  suma_recursiva:           {suma_recursiva(nums)}  (esperado: 28)")
    print(f"  maximo_recursivo:         {maximo_recursivo(nums)}  (esperado: 9)")
    print(f"  cuenta_mayores(umbral=4): {cuenta_mayores_recursivo(nums, 4)}  (esperado: 3)")
    print(f"  suma_recursiva([]):       {suma_recursiva([])}  (esperado: 0)")

    # ---- PARTE 3 ----
    print("\n" + "=" * 60)
    print("PARTE 3: Potencias")
    print("=" * 60)
    pares_prueba = [(2, 10), (3, 5), (5, 0), (7, 3)]
    for base, exp in pares_prueba:
        lenta = potencia_lenta(base, exp)
        rapida = potencia_rapida(base, exp)
        estado = "OK" if lenta == rapida else "ERROR"
        print(f"  [{estado}] {base}^{exp} = {lenta} (rápida={rapida})")

    # ---- PARTE 4 ----
    print("\n" + "=" * 60)
    print("PARTE 4: Top-K Productos")
    print("=" * 60)
    baratos = top_k_baratos(CATALOGO, 3)
    print("Top-3 más baratos:")
    for p in (baratos or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    cat_ord = sorted(CATALOGO, key=lambda p: p['precio'])
    rango = rango_precio(cat_ord, 10.0, 30.0)
    print("\nProductos entre $10 y $30:")
    for p in (rango or []):
        print(f"  {p['nombre']:25} ${p['precio']:.2f}")

    # =============================================================================
    # REFLEXIÓN FINAL — RESPUESTAS DE ANÁLISIS
    # =============================================================================
    print("\n" + "=" * 60)
    print("REFLEXIÓN FINAL")
    print("=" * 60)
    print("""
[ANÁLISIS] Respuestas de análisis integradas:

1. ¿Qué algoritmo de ordenación elegiste en la Parte 1 y por qué es apropiado?
   - Se seleccionó Timsort (mediante la función nativa sorted()). Es apropiado 
     porque ofrece una complejidad eficiente de O(n log n) y es un algoritmo estable 
     que permite ordenar diccionarios utilizando criterios múltiples (apellido y nombre).

2. ¿Cuántas comparaciones haría la búsqueda binaria en una agenda de 1 000 contactos en el peor caso?
   - Como máximo realizaría 10 comparaciones, ya que el espacio de búsqueda se reduce 
     a la mitad iterativamente y se cumple que log2(1000) ≈ 9.96 (redondeando al techo son 10).

3. ¿Cuántas llamadas recursivas hace potencia_rapida(2, 64)?
   - Hace un total de 7 llamadas principales para llegar desde el exponente 64 hasta el 
     caso base (0), siguiendo la secuencia de divisiones: 64 → 32 → 16 → 8 → 4 → 2 → 1 → 0.
""")