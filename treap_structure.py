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

    def representarEnCascada(self, elemento,espacios=0,iteraciones=20):
        espacios += 1
        iteraciones -= 1
        cadena= "-"
        if elemento and iteraciones>0:
            espacios += 3
            cadena = "{}->|{} \n{}|{}".format(elemento.id,self.representarEnCascada(elemento.hijoMenor,espacios,iteraciones),(" "*espacios),self.representarEnCascada(elemento.hijoMayor,espacios,iteraciones))
        
        return cadena

    def buscarUsuario(self, id, elemento):
        cadena = "Buscamos si los hijos coinciden con: ..."
        if elemento.hijoMayor:
            cadena += "el mayor {}".format(elemento.hijoMayor.id)
        if elemento.hijoMenor:
            cadena += "o el menor {}".format(elemento.hijoMenor.id)
        print(cadena)

        # Comparamos el id con el del elemento
        if id > elemento.id:

            print("el que buscamos es mayor")
            # Repetimos la iteración
            if elemento.hijoMayor:
                return self.buscarUsuario(id,elemento.hijoMayor)
            # No lo hemos encontrado
            return None

        if id < elemento.id:

            print("el que buscamos es menor")
            # Repetimos la iteración
            if elemento.hijoMenor:
                return self.buscarUsuario(id,elemento.hijoMenor)
            # No lo hemos encontrado
            return None

        # Si el usuario es el elemento lo retornamos
        print("son iguales")
        return elemento


    def comprobarExistencia(self, id):
        
        elemento = None
        print("buscamos el id ", id)
        for hijo in self.hijos:
            print("intento con el hijo", hijo.id)
            elemento = self.buscarUsuario(id,hijo)
            if elemento:
                print("el elemento era ", elemento.id)
                break
        if elemento:
            print("el elemento es ",elemento.id)
        # Si no existia lo creamos
        if not elemento:
            print("el elemento no es")
            elemento = Usuario(id)
            elemento.padre = self
            self.hijos.append(elemento)

        return elemento


    def anexarRama(self, hijo, padre):

        if padre.id < hijo.id:

            # Si ya existe el hijo aplicamos recurrencia
            if padre.hijoMayor:
                self.anexarRama(hijo,padre.hijoMayor)
            # En caso contrario lo creamos
            else:
                padre.hijoMayor = hijo
                hijo.padre = padre

        else:
            # Igual que para el if
            if padre.hijoMenor:
                self.anexarRama(hijo,padre.hijoMenor)

            else:
                print("añadimos el hijo {} al padre {}".format(hijo.id,padre.id))
                padre.hijoMenor = hijo
                hijo.padre = padre


    def addRelacion(self, id1, id2):

        # Comprobamos si ya están los hijos y donde están
        elemento1 = self.comprobarExistencia(id1)
        elemento2 = self.comprobarExistencia(id2)
        
        # padre = elemento2.padre
        # Aplicamos movimientos para dejar el elemento2 en la cabeza
        # if padre != self:
        #     if padre.id > elemento2.id:
        #         self.movimientoDerecha(elemento2)
        #     else: self.movimientoIzquierda(elemento2)
        raiz2 = self.identificarRaiz(elemento2)
        raiz1 = self.identificarRaiz(elemento1)

        # Eliminamos dicho árbol del registro
        self.hijos.pop(self.hijos.index(raiz2))

        # Anexamos dicho árbol al elemento1
        self.anexarRama(raiz2,raiz1)
        
        print("---------------------------")
        for usuario in self.hijos:
            print(self.representarEnCascada(usuario))
        

    def identificarRaiz(self,elemento):
        if elemento.padre != self:
           return self.identificarRaiz(elemento.padre)

        return elemento



    def movimientoDerecha(self, elemento):
        
        antiguoPadre = elemento.padre
        antiguoHijoMayor = elemento.hijoMayor

        # Definimos una situación por defecto
        nuevoHijoMayor = antiguoPadre
        nuevoNietoMenor = antiguoHijoMayor

        # Cambiamos la situación si el hijoMayor es mayor que el padre
        if antiguoHijoMayor:
            if antiguoHijoMayor.id > antiguoPadre.id:
                nuevoHijoMayor = antiguoHijoMayor
                nuevoNietoMenor = antiguoPadre
        
        # Eliminamos los elementos propios del movimientoDerecha
        elemento.hijoMayor = None
        antiguoPadre.hijoMenor = None

        # Llamamos a movimiento
        self.movimiento(elemento, nuevoHijoMayor, nuevoNietoMenor)
        

    def movimientoIzquierda(self, elemento):
        
        antiguoPadre = elemento.padre
        antiguoHijo = elemento.hijoMenor

        # Definimos una situación por defecto
        nuevoHijo = antiguoPadre
        nuevoNieto = antiguoHijo

        # Cambiamos la situación si el hijoMayor es mayor que el padre
        if antiguoHijo:
            if antiguoHijo.id < antiguoPadre.id:
                nuevoHijo = antiguoHijo
                nuevoNieto = antiguoPadre
        
        # Eliminamos los elementos propios del movimientoIzquierda
        elemento.hijoMenor = None
        antiguoPadre.hijoMayor = None

        # Llamamos a movimiento
        self.movimiento(elemento, nuevoHijo, nuevoNieto)



    def movimiento(self, elemento,nuevoHijo, nuevoNieto):
        
        antiguoPadre = elemento.padre
        antiguoHijo = elemento.hijoMenor

        # Definimos una situación por defecto
        nuevoHijo = antiguoPadre
        nuevoNieto = antiguoHijo

        # Cambiamos la situación si el hijoMayor es mayor que el padre
        if antiguoHijo:
            if antiguoHijo.id < antiguoPadre.id:
                nuevoHijo = antiguoHijo
                nuevoNieto = antiguoPadre
        
        # Redefinimos las relaciones del elemento
        elemento.hijoMenor = None
        elemento.padre = antiguoPadre.padre

        # Borramos las relaciones previas del antiguoPadre
        antiguoPadre.padre = None
        antiguoPadre.hijoMayor = None

        # Introducimos el nuevoHijo
        self.anexarRama(nuevoHijo, elemento)

        # Introducimos el nuevoNieto
        if nuevoNieto:
            self.anexarRama(nuevoNieto,nuevoHijo)
        
        # Comprobamos si es necesario seguir subiendo
        self.recurrenciaDeMovimiento(elemento,antiguoPadre)
        



    def recurrenciaDeMovimiento(self,elemento, antiguoPadre):
        
        # Verificamos si estamos en la cima
        if elemento.padre != self:
            
            # Eliminamos los registros en el abuelo
            if elemento.padre.hijoMenor == antiguoPadre:
                elemento.padre.hijoMenor = None
            else: elemento.padre.hijoMayor = None

            # Determinamos si el elemento es hijoMenor o hijoMayor
            if elemento.padre.id < elemento.id:

                if elemento.padre.hijoMayor:
                    # Debemos mover todo el hijoMayor dentro de nuestra rama
                    self.anexarRama(elemento.padre.hijoMayor, elemento)
                
                # Modificamos los hijos del nuevo padre
                elemento.padre.hijoMayor = elemento

                # Repetimos el proceso
                self.movimientoIzquierda(elemento)                
            
            else:

                if elemento.padre.hijoMenor:
                    # Debemos mover todo el hijoMayor dentro de nuestra rama
                    self.anexarRama(elemento, elemento.padre.hijoMenor)

                elemento.padre.hijoMenor = elemento

                # Repetimos el proceso
                self.movimientoDerecha(elemento)

        # Si estamos en la cima sustituimos el antiguo hijo
        for hijo in self.hijos:
            print(self.representarEnCascada(hijo))
        print("el elemento es: ",antiguoPadre.id)
        for hijo in self.hijos:
            if hijo.id == antiguoPadre.id:
                self.hijos.pop(self.hijos.index(hijo))
        self.hijos.append(elemento)
            