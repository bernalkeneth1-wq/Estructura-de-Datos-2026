class Pila:
    def __init__(self):
        self.datos = []

    def push(self, dato):  # Agrega un elemento
        self.datos.append(dato)

    def pop(self):  # Elimina el último elemento agregado
        if self.is_empty():
            return None
        return self.datos.pop()

    def peek(self):  # Muestra el último elemento agregado
        if self.is_empty():
            return None
        return self.datos[-1]

    def is_empty(self):  # Verifica si la pila está vacía
        return len(self.datos) == 0

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
    print("Caso 2 - Pila despues de push: ", pila2.datos)

    #Caso 3: comprobar peek
    print("Caso 3 - Elemento en el tope:" , pila2.peek())

    #Caso 4: sacar un elemtento con pop
    elemento = pila2.pop()
    print("Caso 4 - Elemento eliminado:" , elemento)
    print("Pila despues de pop:" , pila2.datos)

    #Caso 5: comprobar una pila con varios elementos
    pila3  = Pila()
    pila3.push("A")
    pila3.push("B")
    pila3.push("C")
    print("Caso 5 - Tope de la pila:" ,pila3.peek())