import time

#Definimos nuestra clase de usuario

class Usuario:
    def __init__(self, id):
        self.id = id
        self.rel_dir = []

    def añadir_rel(self, usuario):
        self.rel_dir.append(usuario)

    def obtener_rel(self):
        for rel in self.rel_dir:
            rels = rels + rel.obtene_rel(rel)

#Empezamos leyendo las líneas del documento una a una
def leer_relaciones(fprin):

    # Número de usuarios
    n = 0
    usr = []
    # Lista de conexiones y número de estas
    red = []
    m = 0
    #Leemos el fichero y modificamos nuestro registro
    with open(fprin) as f:
        l = 0
        for linea in f:
            #Recuperamos los valos del número de relaciones y usuarios, aunque no serán usados pues tomaremos los brindados por la función len sobre ambas listas
            if(l==0):
                n = int(linea)
            elif (l == 1):
                rel = int(linea)
                '''try:
                    n = int(linea)
                except:
                    print("El número de usuarios es incorrecto")

            elif (l == 1):
                try:
                    m = int(linea)
                except:
                    print("El número de relaciones es incorrecto")'''
            else:
                palabras = linea.split()
                nu = palabras[0]
                i = 0
                #buscamos si el usuario estaba ya
                for usuario in usr:
                    if (usuario[0] == nu):
                        usuario.append(palabras[1])
                        i = 1
                        break
                if i == 0:
                    usuario = [palabras[0],palabras[1]]
                    usr.append(usuario)
            l = l + 1
        print(usr)
        return [usr,rel]

def ordenacion_influencers(usr):
    usr = sorted(usr, key = len, reverse=True)
    return usr

def main():
    # Preguntar fichero a abrir y porcentaje
    principal = input("Introduzca el nombre del fichero principal.")

    # Leemos el documento y creamos la lista de redes
    tiempo1 = time.time()
    [usr, rel] = leer_relaciones(principal)
    t_leer_doc = time.time() - tiempo1

    # Ordenamos los grumos por tamaño
    tiempo1 = time.time()
    usr = ordenacion_influencers(usr)
    main_usr = usr[0][0]
    t_ordenacion = time.time() - tiempo1

    # Mostrar por pantalla resultados

    #Usuarios conexiones y porcentaje
    print("Número de usuarios: " + str(len(usr))+". "+"Número de relaciones: "+ str(rel) + ".")
    print("El mayor propagador es el usuario {}.".format(main_usr))
    print("Tiene acceso a {} usuarios.".format( str(len(usr[0])-1) ) )


    #Tiempos
    print("Duración leer documento: {:.5f} seg.".format(t_leer_doc))
    print(usr)

main()




