# Creamos dos tipo de árboles uno que contenga los grumos,
# y otro que represente cada grumo y ordene los usuarios dentro de este.

# Comenzamos con
class Usuario:
    def __init__(self, id):
        self.id = id
        self.hijos = []
        self.padre = None

    #Método especial que permite al sort discriminar según el parámetro elegido
    def __lt__(self, other):
        return self.id < other.id


class GrumoTreap:
    def ___init__(self):
        self.hijos = []
        self.id = 0

    def representarEnCascada(self, lista):
        cadena = ""
        for elemento in lista:
            cadena += "{} ".format(elemento.id)
            if len(elemento.hijos) == 1:
                cadena += "->{} ".format(self.representarEnCascada(elemento.hijos))
            elif len(elemento.hijos) != 0:
                cadena += ":({}) ".format(self.representarEnCascada(elemento.hijos))
        return cadena

    def buscarId(self, id, lista):
        # Comprobamos si quedan elementos
        if len(lista) == 0:
            usuario = Usuario(id)
            usuario.__init__(id)
            return usuario

        # Comparamos y bajamos de nivel en el árbol
        elif len(lista) == 1:
            if lista[0].id == id:
                return lista[0]
            return self.buscarId(id, lista[0].hijos)

        # Dividimos la lista en mitades donde centrar la búsqueda

        mitad = len(lista)//2
        mediana = lista[mitad]
        if id < mediana.id:
            # Pasamos la mitad inferior de la lista
            return self.buscarId(id, lista[:mitad])
        elif id > mediana.id:
            # Pasamos la mitad superior de la lista
            return self.buscarId(id, lista[mitad:])
        else:
            # Hemos encontrado el elemento
            return mediana

    def addRelacion(self, id1, id2):
        elemento1 = self.buscarId(id1, self.hijos)
        elemento2 = self.buscarId(id2, self.hijos)
        self.addHijo(elemento2,elemento1)

        # Comprobamos si ya tenía padre el elemento1, si no creamos un grumo
        if elemento1.padre == None:
            elemento1.padre = self
            self.addHijo(elemento1, self)

        # Comprobamos si ya tenía padre el elemento2
        padre = elemento2.padre
        if padre != None:
            # En caso afirmativo quitamos este elemento como newHijo
            padre.hijos.pop(padre.hijos.index(elemento2))
        elemento2.padre = elemento1

        # Devolvemos la estructura de arbol haciendo que los elementos pequeños suban
        print(self.representarEnCascada(self.hijos))
        self.movimientoDerecha(elemento2)

    def movimientoDerecha(self, elemento):
        print("El árbol está así:{}".format(self.representarEnCascada(self.hijos)))
        padre = elemento.padre
        if elemento.id < padre.id:
            abuelo = padre.padre

            # Eliminamos las instancias pasadas
            print("Vamos a eliminar {} de {}".format(padre.id,abuelo.id))
            abuelo.hijos.pop(abuelo.hijos.index(padre))
            padre.hijos.pop(padre.hijos.index(elemento))

            # Redefinimos los padres
            padre.padre = elemento
            elemento.padre = abuelo

            # Añadimos los hijos de abajo a arriba
            self.addHijo(padre,elemento)
            self.addHijo(elemento, abuelo)

            # Comprobamos si sigue siendo menor el elemento que su nuevo padre
            self.movimientoDerecha(elemento)

    def deleteHijo(self,hijo,padre):
        padre.hijos.pop(padre.hijos.index(hijo))
    def addHijo(self,newHijo,padre):

        padre.hijos.append(newHijo)
        listaHijos = sorted(padre.hijos)
        padre.hijos = listaHijos

        print("Ahora son:")
        for elemento in padre.hijos:
            print(elemento.id)
