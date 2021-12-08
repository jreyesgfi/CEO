class NodoArbol:
    def __init__(self, id = None):
        self.id = id
        self.hijoMayor = None
        self.hijoMenor = None
        self.relaciones = []
        self.nuevo = True

    def addUsuario(self,id):
        if self.id == None:
            self.id = id
            return self
        if self.id > id:
            if self.hijoMenor:
                return self.hijoMenor.addUsuario(id)
            self.hijoMenor = NodoArbol(id)
            return self.hijoMenor
        if self.id < id:
            if self.hijoMayor:
                return self.hijoMayor.addUsuario(id)
            self.hijoMayor = NodoArbol(id)
            return self.hijoMayor
        #   Indicamos que el nodo ya existía
        self.nuevo = False
        return self


class Bosque(NodoArbol):
    def ___init__(self):
        #   Llamamos a la clase padre
        super().__init__()

        #   Definimos las raices de nuestros tres árboles
        self.assig = NodoArbol()
        self.conexiones = NodoArbol()
        self.grumos = []

    def addConexion(self,id1, id2):
        #  Añadimos el usuario1 al árbol de conexiones y el usuario2 a sus relaciones
        usuario1 = self.conexiones.addUsuario(id1)
        usuario1.relaciones.append(id2)

        #   También lo hacemos al revés
        usuario2 = self.conexiones.addUsuario(id2)
        usuario2.relaciones.append(id1)

    def construirGrumos(self,raizGrumo,id):

        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(id)
        if usuarioAssig.nuevo:

            #   Añadimos el usuario al árbol del grumo particular
            raizGrumo.addUsuario(id)
            for hijo in self.conexiones.addUsuario(id).relaciones:
                self.construirGrumos(raizGrumo,hijo)
    
    def crearGrumos(self, raizGrumoConex):

        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(raizGrumoConex.id)
        if usuarioAssig.nuevo:

            #   Si no estaba creamos un nuevo grumo
            raizGrumo = NodoArbol(raizGrumoConex.id)
            self.grumos.append(raizGrumo)
            for hijo in raizGrumoConex.relaciones:
                self.construirGrumos(raizGrumo,hijo)

        #   A continuación seguimos descendiendo en el árbol de conexiones
        if raizGrumoConex.hijoMenor:
            self.crearGrumos(raizGrumoConex.hijoMenor)
        if raizGrumoConex.hijoMayor:
            self.crearGrumos(raizGrumoConex.hijoMayor)
    def representarGrumos(self):
        for grumo in self.grumos:
            self.representarEnCascada(grumo)
    def representarEnCascada(self, elemento,espacios=0,iteraciones=20):
        espacios += 1
        iteraciones -= 1
        cadena= "-"
        if elemento and iteraciones>0:
            espacios += 3
            cadena = "{}->|{} \n{}|{}".format(elemento.id,self.representarEnCascada(elemento.hijoMenor,espacios,iteraciones),(" "*espacios),self.representarEnCascada(elemento.hijoMayor,espacios,iteraciones))
        
        return cadena
