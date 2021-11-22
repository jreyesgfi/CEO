# Creamos dos tipo de árboles uno que contenga los grumos,
# y otro que represente cada grumo y ordene los usuarios dentro de este.

#Comenzamos con 
class usuario:
    def __init__(self,id):
        self.id = id
        self.hijos = []
        self.padre = None
class grumoTreap:
    def ___init__(self):
        self.arbol = []

    def buscarId(self,id,lista):

        # Comprobamos si quedan elementos
        if len(lista) == 0:
            return usuario(id)

        # Comparamos y bajamos de nivel en el árbol
        if len(lista) == 1:
            if lista[0].id == id:
                return lista[0]
            self.buscarId(id, lista[0].hijos)
        
        # Dividimos la lista en mitades donde centrar la búsqueda
        mitad = len(lista)//2
        mediana = lista[mitad]
        if id > mediana.id:
            # Pasamos la mitad inferior de la lista
            self.buscarId(id, lista[:mitad])
        elif id < mediana.id:
            # Pasamos la mitad superior de la lista
            self.buscarId(id, lista[mitad:])
        else:
            # Hemos encontrado el elemento
            return mediana

    def addRelacion(self, id1, id2):
        elemento1 = self.buscarId(id1,self.arbol)
        elemento2 = self.buscarId(id2,self.arbol)
        elemento1.hijos.append(elemento2)

        # Comprobamos si ya tenía padre el elemento2
        padre = elemento2.padre
        if padre != None:
            # En caso afirmativo quitamos este elemento como hijo
            padre.hijos.pop(padre.hijos.index(elemento2))
        elemento2.padre = elemento1
