# Creamos dos tipo de árboles uno que contenga los grumos,
# y otro que represente cada grumo y ordene los usuarios dentro de este.

# Comenzamos con
class Usuario:
    def __init__(self, id):
        self.id = id
        self.hijoMayor = None
        self.hijoMenor = None
        self.padre = None

    #Método especial que permite al sort discriminar según el parámetro elegido
    def __lt__(self, other):
        return self.id < other.id


class GrumoTreap:
    def ___init__(self,primerHijo):
        self.hijos = [primerHijo]
        self.id = 0

    def representarEnCascada(self, elemento,espacios):
        espacios += 1
        cadena= "-"
        if elemento:
            espacios += 3
            cadena = "{}->|{} \n {}|{}".format(elemento.id,self.representarEnCascada(elemento.hijoMenor,espacios),(" "*espacios),self.representarEnCascada(elemento.hijoMayor,espacios))
        
        return cadena

    def addUsuario(self, id, elemento):
        
        # Comparamos el id con el del elemento
        if id > elemento.id:

            # Repetimos la iteración
            if elemento.hijoMayor:
                return self.addUsuario(id,elemento.hijoMayor)
            # Creamos el usuario
            elemento.hijoMayor = Usuario(id)
            return elemento.hijoMayor

        if id < elemento.id:

            # Repetimos la iteración
            if elemento.hijoMenor:
                return self.addUsuario(id,elemento.hijoMenor)
            # Creamos el usuario  
            elemento.hijoMenor = Usuario(id)
            return elemento.hijoMenor

        # Si el usuario es el elemento lo retornamos
        return elemento

    def addRelacion(self, id1, id2):
        [elemento1, elemento2] = [self.addUsuario(id1,self.hijos[0]), self.addUsuario(id2,self.hijos[0])]
        print(self.representarEnCascada(self.hijos[0],0))
        
    def movimientoDerecha(self, elemento):
        pass
        
    def movimientoIzquierda(self, elemento):
        pass