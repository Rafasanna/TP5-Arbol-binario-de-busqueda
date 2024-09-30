"""Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;

b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol."""



# Clase para representar un nodo del árbol binario
class Nodo:
    def _init_(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True si es héroe, False si es villano
        self.izquierda = None
        self.derecha = None

# Clase para representar el árbol binario
class ArbolBinario:
    def _init_(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = Nodo(nombre, es_heroe)
        else:
            self._insertar_recursivo(self.raiz, nombre, es_heroe)

    def _insertar_recursivo(self, nodo, nombre, es_heroe):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.izquierda, nombre, es_heroe)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.derecha, nombre, es_heroe)

    # Función para listar villanos en orden alfabético
    def listar_villanos(self):
        villanos = []
        self._listar_villanos_recursivo(self.raiz, villanos)
        villanos.sort()  # Ordenamos alfabéticamente
        print("Villanos ordenados alfabéticamente:")
        for villano in villanos:
            print(villano)

    def _listar_villanos_recursivo(self, nodo, villanos):
        if nodo is not None:
            self._listar_villanos_recursivo(nodo.izquierda, villanos)
            if not nodo.es_heroe:
                villanos.append(nodo.nombre)
            self._listar_villanos_recursivo(nodo.derecha, villanos)

    # Función para mostrar superhéroes que comienzan con C
    def listar_heroes_con_c(self):
        print("Superhéroes que empiezan con 'C':")
        self._listar_heroes_con_c_recursivo(self.raiz)

    def _listar_heroes_con_c_recursivo(self, nodo):
        if nodo is not None:
            self._listar_heroes_con_c_recursivo(nodo.izquierda)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                print(nodo.nombre)
            self._listar_heroes_con_c_recursivo(nodo.derecha)

    # Función para contar superhéroes en el árbol
    def contar_heroes(self):
        return self._contar_heroes_recursivo(self.raiz)

    def _contar_heroes_recursivo(self, nodo):
        if nodo is None:
            return 0
        elif nodo.es_heroe:
            return 1 + self._contar_heroes_recursivo(nodo.izquierda) + self._contar_heroes_recursivo(nodo.derecha)
        else:
            return self._contar_heroes_recursivo(nodo.izquierda) + self._contar_heroes_recursivo(nodo.derecha)

    # Función para corregir el nombre de Doctor Strange
    def corregir_doctor_strange(self):
        print("Buscando y corrigiendo Doctor Strange...")
        self._corregir_nombre_recursivo(self.raiz)

    def _corregir_nombre_recursivo(self, nodo):
        if nodo is not None:
            if 'Strange' in nodo.nombre:
                nodo.nombre = 'Doctor Strange'
                print("Nombre corregido a Doctor Strange.")
            self._corregir_nombre_recursivo(nodo.izquierda)
            self._corregir_nombre_recursivo(nodo.derecha)

    # Función para listar héroes en orden descendente
    def listar_heroes_descendente(self):
        heroes = []
        self._listar_heroes_recursivo(self.raiz, heroes)
        heroes.sort(reverse=True)  # Orden descendente
        print("Superhéroes ordenados de manera descendente:")
        for heroe in heroes:
            print(heroe)

    def _listar_heroes_recursivo(self, nodo, heroes):
        if nodo is not None:
            self._listar_heroes_recursivo(nodo.izquierda, heroes)
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self._listar_heroes_recursivo(nodo.derecha, heroes)

    # Función para generar los bosques de héroes y villanos
    def generar_bosque(self):
        arbol_heroes = ArbolBinario()
        arbol_villanos = ArbolBinario()
        self._generar_bosque_recursivo(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _generar_bosque_recursivo(self, nodo, arbol_heroes, arbol_villanos):
        if nodo is not None:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self._generar_bosque_recursivo(nodo.izquierda, arbol_heroes, arbol_villanos)
            self._generar_bosque_recursivo(nodo.derecha, arbol_heroes, arbol_villanos)

    # Barrido ordenado de cada árbol generado
    def barrido_inorden(self):
        self._barrido_inorden_recursivo(self.raiz)

    def _barrido_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._barrido_inorden_recursivo(nodo.izquierda)
            print(f"Nombre: {nodo.nombre}, Héroe: {nodo.es_heroe}")
            self._barrido_inorden_recursivo(nodo.derecha)

    # Contar nodos de un árbol
    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo.izquierda) + self._contar_nodos_recursivo(nodo.derecha)


# Crear el árbol binario
arbol_mcu = ArbolBinario()

# Insertar superhéroes y villanos
arbol_mcu.insertar('Tony Stark', True)
arbol_mcu.insertar('Steve Rogers', True)
arbol_mcu.insertar('Natasha Romanoff', True)
arbol_mcu.insertar('Thanos', False)
arbol_mcu.insertar('Loki', False)
arbol_mcu.insertar('Carol Danvers', True)
arbol_mcu.insertar('Doctor Strange', True)  # Nombre mal cargado

# a. Listar villanos ordenados alfabéticamente
print("\nActividad b:")
arbol_mcu.listar_villanos()

# b. Mostrar superhéroes que empiezan con 'C'
print("\nActividad c:")
arbol_mcu.listar_heroes_con_c()

# c. Contar cuántos superhéroes hay en el árbol
print("\nActividad d:")
print(f"Cantidad de superhéroes en el árbol: {arbol_mcu.contar_heroes()}")

# d. Corregir el nombre de Doctor Strange
print("\nActividad e:")
arbol_mcu.corregir_doctor_strange()

# e. Listar superhéroes en orden descendente
print("\nActividad f:")
arbol_mcu.listar_heroes_descendente()

# f. Generar bosque de héroes y villanos
arbol_heroes, arbol_villanos = arbol_mcu.generar_bosque()

# g. Determinar cuántos nodos tiene cada árbol
print("\nActividad g.I:")
print(f"Cantidad de nodos en el árbol de héroes: {arbol_heroes.contar_nodos()}")
print(f"Cantidad de nodos en el árbol de villanos: {arbol_villanos.contar_nodos()}")

# h. Barrido ordenado alfabéticamente de cada árbol
print("\nBarrido ordenado de héroes:")
arbol_heroes.barrido_inorden()

print("\nBarrido ordenado de villanos:")
arbol_villanos.barrido_inorden()