"""
Lab 13 — Árbol Binario de Búsqueda (BST)
INF 222 Estructura de Datos · Semestre 2026-2
"""

import random


# =============================================================================
# NODO DEL BST
# =============================================================================

class NodoBST:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


# =============================================================================
# ÁRBOL BINARIO DE BÚSQUEDA
# =============================================================================

class BST:
    """
    Árbol Binario de Búsqueda (Binary Search Tree).
    Invariante: para todo nodo n:
      - todos los nodos del subárbol izquierdo tienen dato < n.dato
      - todos los nodos del subárbol derecho tienen dato > n.dato
    No se almacenan duplicados.
    """

    def __init__(self):
        self._raiz = None

    # ------------------------------------------------------------------
    # INSERCIÓN
    # ------------------------------------------------------------------

    def insertar(self, dato):
        """Inserta `dato` en el BST. Ignora duplicados. O(h)."""
        self._raiz = self._insertar_rec(self._raiz, dato)

    def _insertar_rec(self, nodo, dato):
        """
        Retorna el nodo raíz del subárbol actualizado.
        Caso base: nodo es None → crear hoja nueva.
        Si dato < nodo.dato: insertar en subárbol izquierdo.
        Si dato > nodo.dato: insertar en subárbol derecho.
        Si dato == nodo.dato: no hacer nada (sin duplicados).
        """
        if nodo is None:
            return NodoBST(dato)
        
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar_rec(nodo.derecho, dato)
        
        return nodo

    # ------------------------------------------------------------------
    # BÚSQUEDA
    # ------------------------------------------------------------------

    def buscar(self, dato):
        """Retorna True si `dato` está en el BST, False si no. O(h)."""
        return self._buscar_rec(self._raiz, dato)

    def _buscar_rec(self, nodo, dato):
        """
        Caso base 1: nodo es None → no encontrado.
        Caso base 2: nodo.dato == dato → encontrado.
        Si dato < nodo.dato: buscar en subárbol izquierdo.
        Si dato > nodo.dato: buscar en subárbol derecho.
        """
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        
        if dato < nodo.dato:
            return self._buscar_rec(nodo.izquierdo, dato)
        else:
            return self._buscar_rec(nodo.derecho, dato)

    # ------------------------------------------------------------------
    # MÍNIMO Y MÁXIMO
    # ------------------------------------------------------------------

    def minimo(self):
        """Retorna el dato mínimo del BST. Lanza ValueError si está vacío."""
        if self._raiz is None:
            raise ValueError("árbol vacío")
        return self._minimo_nodo(self._raiz).dato

    def _minimo_nodo(self, nodo):
        """Navega hacia el nodo más a la izquierda (mínimo del subárbol)."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def maximo(self):
        """Retorna el dato máximo del BST."""
        if self._raiz is None:
            raise ValueError("árbol vacío")
        actual = self._raiz
        while actual.derecho is not None:
            actual = actual.derecho
        return actual.dato

    # ------------------------------------------------------------------
    # ELIMINACIÓN
    # ------------------------------------------------------------------

    def eliminar(self, dato):
        """Elimina `dato` del BST si existe. O(h)."""
        self._raiz = self._eliminar_rec(self._raiz, dato)

    def _eliminar_rec(self, nodo, dato):
        """
        Retorna el nodo raíz del subárbol actualizado.

        Hay 3 casos para el nodo a eliminar:
          CASO 1 — Es una hoja (sin hijos):
            → Retornar None (eliminar el nodo).

          CASO 2 — Tiene un solo hijo:
            → Retornar el hijo que existe (el nodo desaparece).

          CASO 3 — Tiene dos hijos:
            → Encontrar el SUCESOR INORDEN (mínimo del subárbol derecho).
            → Copiar el dato del sucesor al nodo actual.
            → Eliminar el sucesor del subárbol derecho.
        """
        if nodo is None:
            return None  # dato no estaba en el árbol

        if dato < nodo.dato:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._eliminar_rec(nodo.derecho, dato)
        else:
            # Encontrado — aplicar los 3 casos
            
            # Caso 1: Nodo sin hijos (hoja)
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            
            # Caso 2: Nodo con un solo hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            # Caso 3: Nodo con dos hijos
            # Encontrar el sucesor inorden (el menor del subárbol derecho)
            sucesor = self._minimo_nodo(nodo.derecho)
            nodo.dato = sucesor.dato
            # Eliminar el sucesor duplicado en el subárbol derecho
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.dato)

        return nodo

    # ------------------------------------------------------------------
    # ALTURA Y TAMAÑO
    # ------------------------------------------------------------------

    def altura(self):
        """Altura del árbol (0 si vacío, 1 si solo raíz). O(n)."""
        return self._altura_rec(self._raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo),
                       self._altura_rec(nodo.derecho))

    def tamanio(self):
        """Número de nodos en el árbol. O(n)."""
        return self._tamanio_rec(self._raiz)

    def _tamanio_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._tamanio_rec(nodo.izquierdo) + self._tamanio_rec(nodo.derecho)

    # ------------------------------------------------------------------
    # RECORRIDOS
    # ------------------------------------------------------------------

    def inorden(self):
        """Retorna lista con los datos en orden ascendente. O(n)."""
        resultado = []
        self._inorden_rec(self._raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorden_rec(nodo.derecho, resultado)

    # ------------------------------------------------------------------
    # ÁRBOL DEGENERADO (comparación)
    # ------------------------------------------------------------------

    def construir_bst_degenerado(self, datos_ordenados):
        """
        Inserta datos_ordenados en orden → produce un árbol como lista enlazada.
        Útil para comparar el caso promedio vs. el peor caso de un BST.
        """
        bst = BST()
        for d in datos_ordenados:
            bst.insertar(d)
        return bst


# =============================================================================
# FUNCIONES DE VISUALIZACIÓN (no modificar)
# =============================================================================

def imprimir_arbol(nodo, prefijo="", es_derecho=True):
    """Imprime el árbol de forma visual rotada 90° (subárbol derecho arriba)."""
    if nodo is not None:
        imprimir_arbol(nodo.derecho, prefijo + ("│   " if es_derecho else "    "), True)
        print(prefijo + ("└── " if es_derecho else "┌── ") + str(nodo.dato))
        imprimir_arbol(nodo.izquierdo, prefijo + ("    " if es_derecho else "│   "), False)


# =============================================================================
# TRABAJO AUTÓNOMO: EXPLICACIÓN Y DIAGRAMA DE ROTACIÓN SIMPLE EN AVL
# =============================================================================
"""
EXPLICACIÓN DE LA ROTACIÓN SIMPLE (DERECHA / IZQUIERDA EN ÁRBOLES AVL):
-----------------------------------------------------------------------
Una rotación simple es una operación local de reestructuración que se realiza 
cuando un árbol AVL pierde el balance (es decir, el factor de balance de algún 
nodo se sale del rango {-1, 0, 1})[span_1](start_span)[span_1](end_span).

- Rotación Simple a la Derecha (LL - Left-Left): Se aplica cuando el desbalance 
  es causado por una inserción en el subárbol izquierdo del hijo izquierdo. 
  El nodo desbalanceado pasa a ser el hijo derecho de su antiguo hijo izquierdo, 
  ajustando las referencias de los subárboles intermedios para mantener la 
  propiedad de orden del BST.

Diagrama propio (Rotación Simple a la Derecha):

      Desbalanceado (z)                        Balanceado (y)
           /                                       /   \\
         (y)  <-- Inserción Izq-Izq              (x)    (z)
         /                                       / \\   / \\
       (x)                                      A   B  C   D
       / \\
      A   B

Donde las alturas se reajustan eficientemente en tiempo O(1) manteniendo 
la propiedad de búsqueda binaria y restaurando el factor de balance a {-1, 0, 1}.
"""