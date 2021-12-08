import time
import treap_structure_final as treap

#   Definimos nuestro bosque que contiene todos nuestros árboles
bosque = treap.Bosque()
bosque.___init__()


#Empezamos leyendo las líneas del documento una a una
def leer_relaciones(fprin):

    #   Leemos el fichero y modificamos nuestro registro
    with open(fprin) as f:
        l = 0
        for linea in f:
            #   Recuperamos los valos del número de relaciones y usuarios, aunque no serán usados pues tomaremos los brindados por la función len sobre ambas listas
            if(l == 0):
                n = int(linea)
            elif (l == 1):
                m = int(linea)
            else:
                #   Definimos una nueva relación
                pareja = linea.split()
                bosque.addConexion(pareja[0],pareja[1])
            l = l + 1


    # if fextra != "":
    #     with open(fextra) as f:
    #         for linea in f:
    #             nr = []
    #             for palabra in linea.split():
    #                 nr.append(int(palabra))
    #                 '''try:
    #                     nr.append(int(palabra))
    #                 except:
    #                     print("La relación de una pareja de elementos es incorrecta")'''
    #             if (len(nr) == 2):
    #                 red.append(nr)
    # return (red)

def seleccion_grumos(grus,usr,porcen):
    pass
def main():
    # Preguntar fichero a abrir y porcentaje
    principal = input("Introduzca el nombre del fichero principal.")
    #   extra = input("Introduzca el nombre del fichero extra o pulse ENTER.")
    porcen = float(input("Introduzca el porcentaje deseado")) / 100

    # Leemos el documento y construimos el árbol conexión
    tiempo1 = time.time()
    leer_relaciones(principal)
    t_leer_doc = time.time() - tiempo1

    # Construimos los grumos como árboles
    tiempo1=time.time()
    bosque.crearGrumos(bosque.conexiones)
    t_lista_grumos = time.time() - tiempo1

    # Selección de grumos
    #

    #---MOSTRAR POR PANTALLA RESULTADOS---#

    #Usuarios conexiones y porcentaje
    #   print("Número de usuarios: " + str(len(usr))+". "+"Número de relaciones: "+ str(len(red)) + ".")
    print("Tamaño en porcentaje del mayor grumo deseado: " + str(porcen*100) + "%.")

    #Tiempos
    print("Duración leer documento: {:.5f} seg.".format(t_leer_doc))
    print("Duración creación lista grumos: {:.5f} seg.".format(t_lista_grumos) )

    #Ranking grumos
    print("Existen {} grumos.".format( len(bosque.grumos) ) )
    i = 0
    for porcentaje in bosque.obtenerPorcentajes():
        i += 1
        print("El porcentaje del grumo {} es {:.2f}".format(i,porcentaje))

    #Recomendaciones de uniones
main()




