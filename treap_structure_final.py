



# Método de ordenamiento con medianas
def addElementoMediana(listaTotal,elemento,lista,pos=0):
        # Si se ha acabado la lista metemos nuestro elemento
        if len(lista)==0:
            listaTotal.insert(pos,elemento)
            return

        # Determinamos la mediana para comparar
        mitad = len(lista)//2
        mediana = lista[mitad][1]
        if len(lista)%2==0:
            mediana = (mediana + lista[mitad-1][1])/2

        # Elegimos a cual de las dos mitades pertenece nuestro nuevo elemento
        if mediana < elemento[1]:
            addElementoMediana(listaTotal,elemento,lista[:mitad],pos)
            return
        # Incrementamos la posición  
        pos += mitad + 1

        if mediana > elemento[1]:
            # Si pertenece a la segunda mitad sumamos la posición  
            addElementoMediana(listaTotal,elemento,lista[mitad+1:],pos)
            return
        else:
            addElementoMediana(listaTotal,elemento,[],pos)
            return
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
        # self.maxNivel = 0

    def addConexion(self,id1, id2):
        
        #  Añadimos el usuario1 al árbol de conexiones y el usuario2 a sus relaciones
        usuario1 = self.conexiones.addUsuario(id1)
        usuario1.relaciones.append(id2)
        # if usuario1.nivel > self.maxNivel:
        #         self.maxNivel = usuario1.nivel
        #         print(self.maxNivel)

        #   También lo hacemos al revés
        usuario2 = self.conexiones.addUsuario(id2)
        usuario2.relaciones.append(id1)
        # if usuario2.nivel > self.maxNivel:
        #     self.maxNivel = usuario2.nivel
        #     print(self.maxNivel)


    def construirGrumos(self,grumo,id):
        raizGrumo = grumo[0]
        
        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(id)
        if usuarioAssig.nuevo:

            #   Añadimos el usuario al árbol del grumo particular y aumentamos el tamaño
            usuarioGrumo = raizGrumo.addUsuario(id)
            # if usuarioGrumo.nivel > self.maxNivel:
            #     self.maxNivel = usuarioGrumo.nivel
            #     print(self.maxNivel)

            grumo[1] += 1

            #   Iteramos sobre sus relaciones
            for hijo in self.conexiones.addUsuario(id).relaciones:
                self.construirGrumos(grumo,hijo)
    
    def crearGrumos(self, raizGrumoConex):

        # comprobar si usuario esta asig y si no lo añadimos
        usuarioAssig = self.assig.addUsuario(raizGrumoConex.id)
        if usuarioAssig.nuevo:
            #   Si no estaba creamos un nuevo grumo: raíz y tamaño
            grumo = [NodoArbol(raizGrumoConex.id), 1]
            for hijo in raizGrumoConex.relaciones:
                self.construirGrumos(grumo,hijo)
            addElementoMediana(self.grumos,grumo,self.grumos)

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
            numUsuarios += grumo[1]
            numGrumos += 1
        return [numUsuarios,numGrumos]

