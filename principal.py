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

def seleccion_grumos(bosque, porcen):
    grumosSeleccionados = bosque.obtenerPorcentajes(porcen)
    #  Salvamos las nuevas relaciones
    f = open("extra.txt","w") #De esta forma se borra automáticamente el anterior extra.txt
    grumoPasado = None
    for grumo in grumosSeleccionados:
        # Comprobamos que no estamos en el primer grupo
        if grumoPasado != None:
            # Proponemos la nueva relación
            f.write(grumo['raiz'].id+" "+grumoPasado['raiz'].id+"\n")
        # Definimos el nuevo grumo
        grumoPasado = grumo
        
            


    return grumosSeleccionados

def main():
    # Preguntar fichero a abrir y porcentaje
    principal = input("Introduzca el nombre del fichero principal:\n")
    #   extra = input("Introduzca el nombre del fichero extra o pulse ENTER.")
    porcen = float(input("Introduzca el porcentaje deseado:\n")) / 100

    # Leemos el documento y construimos el árbol conexión
    tiempo1 = time.time()
    leer_relaciones(principal)
    t_leer_doc = time.time() - tiempo1

    # Construimos los grumos como árboles
    tiempo1=time.time()
    bosque.crearGrumos(bosque.conexiones)
    t_lista_grumos = time.time() - tiempo1

    # Selección de grumos
    tiempo1=time.time()
    grumosSeleccionados = seleccion_grumos(bosque, porcen)
    t_seleccion_grumos = time.time() - tiempo1



    #---MOSTRAR POR PANTALLA RESULTADOS---#

    #   Usuarios conexiones y porcentaje
    #   print("Número de usuarios: " + str(len(usr))+". "+"Número de relaciones: "+ str(len(red)) + ".")
    print("Tamaño en porcentaje del mayor grumo deseado: " + str(porcen*100) + "%.")

    #   Tiempos
    print("Duración leer documento: {:.5f} seg.".format(t_leer_doc))
    print("Duración creación lista grumos: {:.5f} seg.".format(t_lista_grumos) )
    print("Duración selección grumos: {:.5f} seg.".format(t_seleccion_grumos) )

    #   Ranking grumos
    print("Existen {} grumos.".format( len(bosque.grumos) ) )

    #   Recuperamos cada uno de los porcentajes de los grumos
    i = 0
    for grumo in grumosSeleccionados:
        i += 1
        print("El porcentaje del grumo {} es {:.2f}".format(i,grumo['porcentaje']))


    #   Recomendaciones de uniones
    if len(grumosSeleccionados) !=1:
        print("Las nuevas relaciones de amistad (salvadas en extra.txt) son:")
        with open("extra.txt") as f:
            for linea in f:
                pareja = linea.split()
                print("{} con {}.".format(pareja[0],pareja[1]))
    else:
        print("No hacen falta nuevas relaciones de amistad.")
main()




