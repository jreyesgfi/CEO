class NodoArbol:
    def __init__(self, id):
        self.id = id
        self.hijoMayor = None
        self.hijoMenor = None
        self.relaciones = []
        self.nuevo = True

    def addRelacion(self,usrToFind,usrAmigo):
        usr = self.addUsuario(self,usrToFind)
        usr.relaciones.append(usrAmigo)

    def addUsuario(self,id):
        if self.id > id:
            if self.hijoMenor:
                return self.addUsuario(self.hijoMenor,id)
            self.hijoMenor = NodoArbol(id)
            return self.hijoMenor
        if self.id < id:
            if self.hijoMayor:
                return self.addUsuario(self.hijoMayor,id)
            self.hijoMayor = NodoArbol(id)
            return self.hijoMayor
        #   Indicamos que el nodo ya existía
        self.nuevo = False
        return self


class ArbolConexiones(NodoArbol):
    def ___init__(self,rel):
        #   Llamamos a la clase padre
        super().__init__()

        #   Definimos las raices de nuestros tres árboles
        self.assig = None
        self.conexiones = None
        self.grumos = None

    def addConexion(self,id1, id2):
        #  Añadimos el usuario1 al árbol de conexiones y el usuario2 a sus relaciones
        usuario1 = self.conexiones.addUsuario(id1)
        usuario1.relaciones.append(id2)

    def construirGrumos(self,raizGrumo,usuarioConex):

        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(usuarioConex.id)
        if usuarioAssig.nuevo:

            #   Añadimos el usuario al árbol del grumo particular
            raizGrumo.addUsuario(usuarioConex.id)
            for hijo in usuarioConex.relaciones:
                self.construirGrumos(raizGrumo,hijo)
    
    def crearGrumos(self, raizGrumoConex):

        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(raizGrumoConex.id)
        if usuarioAssig.nuevo:

            #   Si no estaba creamos un nuevo grumo
            raizGrumo = self.grumos.addUsuario(raizGrumoConex.id)
            for hijo in raizGrumoConex.relaciones:
                self.construirGrumos(raizGrumo,hijo)

        #   A continuación seguimos descendiendo en el árbol de conexiones
        if raizGrumoConex.hijoMenor:
            self.crearGrumos(raizGrumoConex.hijoMenor)
        if raizGrumo.hijoMayor:
            self.crearGrumos(raizGrumoConex.hijoMayor)
