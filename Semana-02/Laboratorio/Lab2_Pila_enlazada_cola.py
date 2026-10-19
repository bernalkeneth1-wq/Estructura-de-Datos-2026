#=================================================
#1. NODO (Base para la pila enlazada y la cola)
#=================================================
class Nodo:
    """Un nodo guarda un dato y un puntero al siguiente nodo."""
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

#===================
#2. Pila Enlazada
#===================

class Pila:
    """Una pila enlazada es una estructura de datos que sigue el principio LIFO (Last In, First Out).

    cima -> [3] ->[2] -> [1] -> None
    3 es el ultimo elemento agregado a la pila, por lo tanto es el primero en salir."""

    def __init__(self):
        self._cima = None
        self._tamaño = 0

    def push(self, dato):
        """Agrega un nuevo nodo a la cima de la pila con el dato proporcionado."""
        nuevo_nodo = Nodo(dato, self.cima)
        self.cima = nuevo_nodo
        self.tamaño += 1


    def pop(self):
        """Elimina y devuelve el dato del nodo en la cima de la pila.
        Lanza IndexError si la pila esta vacia."""
        if self.cima is None:
            raise IndexError
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamaño -= 1
        return dato

    def peek(self):
        """Retorna sin eliminar el dato del tope. Lanza IndexError si esta vacia."""
        if self._cima is None:
            raise IndexError
        return self._cima.dato

    def is_empty(self):
        """Devuelve True si la pila esta vacia, de lo contrario devuelve False."""
        return self._cima is None

    def size(self):
        """Devuelve el numero de elementos en la pila."""
        return self._tamaño
    
    def __str__(self):
        """Devuelve una representacion en cadena de la pila."""
        elementos = []
        actual = self.cima
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) + " -> None"

    def __len__(self):
        """Devuelve el numero de elementos en la pila."""
        return self.tamaño

#===========================================
#3. verificador de parentesis balanceados
#===========================================

def parentesis_balanceados(cadena):
    """Verifica si los parentesis en cadena estan balanceados."""
    pila = Pila()

    pares = {')': '(',']': '[', '}':'{'}
    aperturas = set(pares.values())

    for caracter in cadena:
        if caracter in aperturas:
            pila.push(caracter)

        elif caracter in pares:
            if pila.is_empty():
                return False
            if pila.peek() != pares[caracter]:
                return False
                
                pila.pop()

    return pila.is_empty()

#===================================
#4. Cola (FIFO) con nodos enlazados
#===================================
class Cola:

    """Cola FIFO: frente -> [1] -> [2] -> [3] -> None <- final.
    
    se mantiene referencia al frente y al final para que enqueue y dequeue sean 0(1).
    """
    def __init__(self):
        self._frente = None
        self._final = None
        self._tamaño = 0

    def enqueue(self, dato):
        """Agrega dato al final de la cola. Complejidad: 0(1)."""
        nuevo = Nodo(dato)

        if self._frente is None: #fila vacia
            self._frente = nuevo
            self._final = nuevo
        else:                   #fila con gente
            self._final.siguiente = nuevo
            self._final = nuevo

        self._tamaño += 1

    def dequeue(self):
        """Elimina y retorna el dato del frente. Lanza IndexError si esta vacia."""
        if self._frente is None:
           raise IndexError("La cola esta vacia")
        
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        self._tamaño -= 1

        if self._frente is None:
            self._final = None
        
        return dato

    def front(self):
        """Retorna (sin eliminar) el dato del frente. Lanza IndexError si esta vacia."""
        if self.frente is None:
            raise IndexError("La cola esta vacia")
        
        return self._frente.dato
    
    def is_empty(self):
        return self._frente is None

    def size(self):
        return self._tamaño

    def __str__ (self): 
        """Representacion frente --> ... --> final"""
        elementos  = []
        actual = self._frente

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = self.siguiente

            return" --> ".join(elementos)

#==================================
#5. Simulador de Cola de impresion 
#==================================

class TrabajoImpresion:
    """Representa un trabajo en la cola de impresion."""

    def __init__(self, nombre, pagina):
        self.nombre = nombre
        self.paginas = pagina

    def __str__(self):
        return f"'{self.nombre}' ({self.paginas} pag.)"

def simulador_impresion(trabajos):
    """
    Simula una cola de impresion. recibe una lista de tuplas (nombre, paginas).
    Imprime en orden de llegada (FIFO) el nombre de cada trabajo y cuantas paginas tienee.
    Al final muestra el total de paginas impresas.
    """
        
    cola =  Cola()
    total_paginas = 0

    for nombre, paginas in trabajos:
        cola.enqueue(TrabajoImpresion(nombre, paginas))

    while not cola.is_empty():
        trabajo = cola.dequeue()
        print(f"Imprimiendo: {trabajo}")
        total_paginas += trabajo.paginas

        print(f"Total de paginas impresas: {total_paginas}")

#==================
#Casos de Pruebas
#==================

if __name__ == "__main__":
    print("=" * 55)
    print("PARTE 2: Pila Enlazada")
    print("=" * 55)

    pila = Pila()

    pila.push(10)
    pila.push(20)
    pila.push(30)

    print("Pila:", pila)
    print("Peek:", pila.peek())
    print("Pop:",pila.pop())
    print("Pila despues del pop:", pila)
    print("¿Esta vacia?:", pila.is_empty())
    print("Tamaño:", pila.size())

    print("\n" + "=" * 55)
    print("PARTE 3. Verificador de Parentisis Balanceados")
    print("=" * 55)
    casos = [
        ("({[]})", True),
        ("([)]", False),
        ("{[", False),
        ("", True),    #cadena vacia: balanceada por vacio

        ("3 + (4 * [2])", True),
    ]

    for cadena, esperado in casos:
        resultado = parentesis_balanceados(cadena)
        estado = "OK" if resultado == esperado else "ERROR"
        print(f" [{estado}] '{cadena}' --> {resultado} (esperado: {esperado})")

    print("\n" + "=" * 55)
    print("PARTE 4. Cola")
    print("=" * 55)

    cola = Cola()

    #Prueba de cola
    cola.enqueue("Tarea 1")
    cola.enqueue("Tarea 2")
    cola.enqueue("Tarea 3")
    print("Cola:", cola)
    print("Front:", cola.front())
    print("Dequeue:", cola.dequeue())
    print("Cola despues de dequeue:", cola)
    print("¿Esta vacia?:", cola.is_empty())
    print("Tamaño:", cola.size())

    print("\n" + "=" * 55)
    print("PARTE 5. Simjulador de Impresion")
    print("=" * 55)

    trabajos = [("Tesis cap1", 12), ("Factura", 1) ("Informe anual", 8), ("CV",2)]
    simulador_impresion(trabajos)