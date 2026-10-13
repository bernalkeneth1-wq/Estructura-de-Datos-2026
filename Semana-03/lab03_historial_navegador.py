class Pila:
    """Implementacion de una pila usando una lista de Python."""
    def __init__(self):
        self._datos = []

    def push(self, dato):
        """Agrega un elemento a la cima de la pila."""
        self._datos.append(dato)

    def pop(self):
        """Retira y devuelve el elemento de la cima."""
        if self.is_empty():
            raise IndexError("pop en pila vacia")
        return self._datos.pop()

    def peek(self):
        """Devuelve el elemento de la cima sin retirarlo."""
        if self.is_empty():
           raise IndexError("peek en la pila vacia")
        return self._datos[-1]

    def is_empty(self):
        """Indica si la pila esta vacia."""
        return len(self._datos) == 0
    
    def size(self):
        """Devuelve la cantidad de elementos de la pila."""
        return len(self._datos)

    def __str__(self):
        return f"Pila (tope->base): {list(reversed(self._datos))}"

#=====================================
#SIMULADOR DE HISTORIAL
#=====================================

class HistorialNavegador:
    """"Simula el historial de un navegador web con botones Atras y Adelante."""

    def __init__(self, pagina_inicial="about:blank"):
        self._actual = pagina_inicial
        self._pila_atras = Pila()
        self._pila_adelante = Pila()

    def visitar(self, url):
        """
        Visita una nueva URL.
        - La pagina actual pasa a la pila de atras.
        - La pila de adelante se vacia.
        """
        self._pila_atras.push(self._actual)
        self._actual = url
        self._pila_adelante = Pila()

    def atras(self):
        """
        Navega a la siguiente pagina(si existe).
        Retorna la URL a la que se navego, o None si no hay pagina siguiente.
        """
        if self._pila_adelante.is_empty():
            return None

        self._pila_atras.push(self.actual)
        self._actual = self._pila_adelante.pop()
        return self._actual
    
    def pagina_actual(self):
        """Rerorna la URL de la pagina actualmente visible."""
        return self._actual
    
    def estado(self):
        """Imprime el estado completo del historial para depuracion."""
        print(f"  Actual:  {self._actual}")
        print(f"  Atras:   {self._pila_atras}")
        print(f"  Adelante: {self._pila_adelante}")

#==============================[=============
#CASOS DE PRUEBA
#=============================================

if __name__ == "__main__":
    print("=" * 55)
    print("Simulador de Historial de Navegador")
    print("=" * 55)

    nav = HistorialNavegador()

    print("\n--- Visitando paginas ---")
    nav.visitar("google.com")
    nav.visitar("wikipedia.org")
    nav.visitar("github.com")
    nav.visitar("up.ac.pa")
    print(f"Pagina actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Navegando Atras x2 ---")
    print(f"  -> {nav.atras()}")
    print(f"  -> {nav.atras()}")
    print(f"Pagina actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Navegando Adelante x1 ---")
    print(f"  -> {nav.adelante()}")
    print(f"Pagina actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Visitar nueva pagina (borra el adelante) ---")
    nav.visitar("classroom.github.com")
    print(f"Pagina actual: {nav.pagina_actual()}")
    nav.estado()

    print("\n--- Intentar adelante cuando no hay ---")
    resultado = nav.adelante()
    print(f" ->{resultado} (esperado: None)")

    print("\n--- Intentar atras hasta el inicio ---")
    while nav.atras() is not None:
        pass
    print(f"Pagina actual: {nav.pagina_actual()} (esperado: about:blank)")
    resultado_extra = nav.atras()
    print(f"Otro atras -> {resultado_extra} (esperado: None)")

