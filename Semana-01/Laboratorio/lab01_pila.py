class Pila:
    def __init__(self):
        self.datos = [] # el tope de la pila esta en el indice -1

    def push(self, dato):  # Agrega 'dato' al tope de la pila.
        """
        Complejidad: 0(1) amortizado.
        """
        self.datos.append(dato)

    def pop(self):  # Elimina el último elemento agregado
        if self.is_empty():
             raise IndexError("La pila esta vacia")
        return self.datos.pop()
    
    def peek(self):  # Muestra el último elemento agregado
        if self.is_empty():
            raise IndexError("La pila esta vacia")
        return self.datos[-1]

    def is_empty(self):  # Verifica si la pila está vacía
        return len(self.datos) == 0

    def size(self): #Retorna el numero de elementos en la pila
        """
        Complejidad: 0(1).
        """
        return len(self.datos)


    def __str__(self): #Retorna una representacion legible de la pila.
        """
        Complejidad: 0(n)
        """
        return f"Pila (tope -> base): {self.datos[::-1]}"

#==================
#CASOS DE PRUEBAS
#==================

if __name__ == "__main__":

    #Caso 1: comprobar que la pila esta vacia
    pila1 =Pila()
    print(f"¿La pila está vacía? {pila1.is_empty()}")

    #Caso 2: agregar elementos con push
    pila2 = Pila()
    pila2.push(10)
    pila2.push(20)
    pila2.push(30)
    print(f"Caso 2 - Tamaño de la pila (size)): {pila2.size()}")
    print("Caso 2 - Elementos en la Pila:" , pila2.datos)

    #Caso 3: peek sin modificar la pila
    print("Caso 3 - Elemento en el tope:" , pila2.peek())
    print("Caso 3 - Pila despues de peek (verifica que no cambia):", pila2.datos)

    #Caso 4: pop retorna al tope
    elemento_eliminado = pila2.pop()
    print(f"Caso 4 - Elemento retornado por pop: {elemento_eliminado}")
    print("Caso 4 - Pila despues del pop:", pila2.datos)

    #Caso 5: pop  en al pila vacia lanza IndexError
    pila3  = Pila()
    try:
        pila3.pop()
    except IndexError as e:
        print("Caso 5 - ¡Excepcion atrapada con exito! Se lanzo  IndexError al intentar hacer pop en una pila vacia.")