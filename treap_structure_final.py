
class NodoArbol:
    def __init__(self, id = None):
        self.id = id
        self.hijoMayor = None
        self.hijoMenor = None
        self.relaciones = []
        self.nuevo = True

    def addUsuario(self,id):
        try:
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

        #   Si self.id = None entoces estamos en la raiz
        except:
            self.id = id
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

    def addGrumo(self,grumo,grumos):
        mitad = len(grumos)//2
        mediana = grumos[mitad]
        if mediana[1] > grumo[1]:
            self.addGrumo(self,grumo,grumos[:mitad])

    def construirGrumos(self,grumo,id):
        raizGrumo = grumo[0]
        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(id)
        if usuarioAssig.nuevo:

            #   Añadimos el usuario al árbol del grumo particular y aumentamos el tamaño
            raizGrumo.addUsuario(id)
            grumo[1] += 1

            #   Iteramos sobre sus relaciones
            for hijo in self.conexiones.addUsuario(id).relaciones:
                self.construirGrumos(grumo,hijo)
    
    def crearGrumos(self, raizGrumoConex):

        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(raizGrumoConex.id)
        if usuarioAssig.nuevo:
            #   Si no estaba creamos un nuevo grumo: raíz y tamaño
            grumo = [NodoArbol(raizGrumoConex.id), 0]
            for hijo in raizGrumoConex.relaciones:
                self.construirGrumos(grumo,hijo)
            se

        #   A continuación seguimos descendiendo en el árbol de conexiones
        if raizGrumoConex.hijoMenor:
            self.crearGrumos(raizGrumoConex.hijoMenor)
        if raizGrumoConex.hijoMayor:
            self.crearGrumos(raizGrumoConex.hijoMayor)


    #----MÉTODOS DE REPRESENTACIÓN---#  
    def representarGrumos(self):
        for grumo in self.grumos:
            print(self.representarEnCascada(grumo[0]))
    def representarEnCascada(self, elemento,espacios=0,iteraciones=20):
        
        espacios += 1
        iteraciones -= 1
        cadena= "-"
        if elemento and iteraciones>0:
            espacios += 3
            cadena = "{}->|{} \n{}|{}".format(elemento.id,self.representarEnCascada(elemento.hijoMenor,espacios,iteraciones),(" "*espacios),self.representarEnCascada(elemento.hijoMayor,espacios,iteraciones))
        return cadena

    def seleccionarGrumos(self,porcentaje):
        tamañoTotal = self.numUsuarios()[0]
        grumosSeleccionados = []
        
        #   Ordenamos los grumos por tamaño
        self.grumos.sort(key= lambda grumo : grumo[1], reverse = True)

        for grumo in self.grumos:
            grumoPorcentaje = grumo[1]/tamañoTotal
            grumosSeleccionados.append(grumo)

            #   Comprobamos si hemos llegado al porcentaje necesario
            porcentaje -= grumoPorcentaje
            if porcentaje <= 0:

                # Si es así los devolvemos
                return grumosSeleccionados

    def numUsuarios(self):
        numUsuarios = 0
        numGrumos = 0
        for grumo in self.grumos:
            numUsuarios += grumo[1] + 1
            numGrumos += 1
        return [numUsuarios,numGrumos]

