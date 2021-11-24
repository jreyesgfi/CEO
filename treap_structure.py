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
            cadena = "{}->|{} \n{}|{}".format(elemento.id,self.representarEnCascada(elemento.hijoMenor,espacios),(" "*espacios),self.representarEnCascada(elemento.hijoMayor,espacios))
        
        return cadena

    def buscarUsuario(self, id, elemento):
        cadena = "Buscamos si los hijos coinciden con: ..."
        if elemento.hijoMayor:
            cadena += "el mayor {}".format(elemento.hijoMayor.id)
        if elemento.hijoMenor:
            cadena += "o el menor {}".format(elemento.hijoMenor.id)
        # print(cadena)

        # Comparamos el id con el del elemento
        if id > elemento.id:

            # print("el que buscamos es mayor")
            # Repetimos la iteración
            if elemento.hijoMayor:
                return self.buscarUsuario(id,elemento.hijoMayor)
            # No lo hemos encontrado
            return None

        if id < elemento.id:

            # print("el que buscamos es menor")
            # Repetimos la iteración
            if elemento.hijoMenor:
                return self.buscarUsuario(id,elemento.hijoMenor)
            # No lo hemos encontrado
            return None

        # Si el usuario es el elemento lo retornamos
        # print("son iguales")
        return elemento

    # def addUsuario(self, newUsuario, usuarioPadre):

    #     # Comparamos el id con el del usuarioPadre
    #     if newUsuario.id > usuarioPadre.id:

    #         # Repetimos la iteración
    #         if usuarioPadre.hijoMayor:
    #             return self.addUsuario(newUsuario,usuarioPadre.hijoMayor)
    #         # Creamos el usuario
    #         usuarioPadre.hijoMayor = newUsuario
    #         newUsuario.padre = usuarioPadre
    #         return usuarioPadre.hijoMayor

    #     if newUsuario < usuarioPadre.id:

    #         # Repetimos la iteración
    #         if usuarioPadre.hijoMenor:
    #             return self.addUsuario(newUsuario,usuarioPadre.hijoMenor)
    #         # Creamos el usuario  
    #         usuarioPadre.hijoMenor = newUsuario
    #         newUsuario.padre = usuarioPadre
    #         return usuarioPadre.hijoMenor

    #     # Si el usuario es el usuarioPadre lo retornamos
    #     return usuarioPadre

    def comprobarExistencia(self, id):
        
        elemento = None
        # print("buscamos el id ", id)
        for hijo in self.hijos:
            # print("intento con el hijo", hijo.id)
            elemento = self.buscarUsuario(id,hijo)
            if elemento:
                # print("el elemento era ", elemento.id)
                break
        # if elemento:
            # print("el elemento es ",elemento.id)
        # Si no existia lo creamos
        if not elemento:
            # print("el elemento no es")
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
                # print("añadimos el hijo {} al padre {}".format(hijo.id,padre.id))
                padre.hijoMenor = hijo
                hijo.padre = padre


    def addRelacion(self, id1, id2):

        # Comprobamos si ya están los hijos y donde están
        elemento1 = self.comprobarExistencia(id1)
        elemento2 = self.comprobarExistencia(id2)

        # Movemos el elemento2 a ser hijo del elemento1

        # Eliminamos el anterior registro
        padre = elemento2.padre
        if padre == self:
            self.hijos.pop(self.hijos.index(elemento2))
        else:
            if padre.id > elemento2.id:
                self.movimientoDerecha(elemento2)
            else: self.movimientoIzquierda(elemento2)
        
        # Creamos el nuevo registro
        self.anexarRama(elemento2,elemento1)
        
        for usuario in self.hijos:
            print(self.representarEnCascada(usuario,0))
        
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
        
        # Realizamos los cambios
        antiguoPadre.hijoMenor = None
        elemento.padre = antiguoPadre.padre

        elemento.hijoMayor = nuevoHijoMayor
        if nuevoNietoMenor:
            self.anexarRama(nuevoNietoMenor,nuevoHijoMayor)

        # Verificamos si estamos en la cima
        if elemento.padre != self:
            

            # Comprobamos si su nuevo padre es mayor o menor
            if elemento.padre.id < elemento.id:

                if elemento.padre.hijoMayor:
                    # Debemos mover todo el hijoMayor dentro de nuestra rama
                    self.anexarRama(elemento, elemento.padre.hijoMayor)
                
                elemento.padre.hijoMayor = elemento

                # Repetimos el proceso
                self.movimientoIzquierda(elemento)                
            
            else:
                elemento.padre.hijoMenor = elemento

                # Repetimos el proceso
                self.movimientoDerecha(elemento) 
            
                
        
    def movimientoIzquierda(self, elemento):
        elemento.padre.hijoMayor = None