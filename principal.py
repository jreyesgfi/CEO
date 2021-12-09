import time
import treap_structure_final as treap




#   Definimos nuestro bosque que contiene todos nuestros árboles
bosque = treap.Bosque()
bosque.___init__()


#Empezamos leyendo las líneas del documento una a una
def leer_relaciones(fprin, fextra):

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


    if fextra != "":
        with open(fextra) as f:
            for linea in f:
                #   Definimos una nueva relación
                pareja = linea.split()
                bosque.addConexion(pareja[0],pareja[1])

def salvar_nuevas_relaciones(grumosSeleccionados):
    print('Guardando nueva relación...')

    #  Salvamos las nuevas relaciones
    f = open("extra.txt","w") #De esta forma se borra automáticamente el anterior extra.txt
    grumoPasado = None

    for grumo in grumosSeleccionados:

        # Comprobamos que no estamos en el primer grupo
        if grumoPasado != None:
            # Proponemos la nueva relación
            f.write(grumo[0].id+" "+grumoPasado[0].id+"\n")

        # Definimos el nuevo grumo
        grumoPasado = grumo

def main():
    # Preguntar fichero a abrir y porcentaje
    principal = input("Introduzca el nombre del fichero principal:  ")
    extra = input("Introduzca el nombre del fichero extra o pulse ENTER:  ")
    porcen = float(input("Introduzca el porcentaje deseado:  ")) / 100

    # Leemos el documento y construimos el árbol conexión
    tiempo1 = time.time()
    leer_relaciones(principal, extra)
    print("reseteamos relaciones")
    bosque.maxNivel = 0
    t_leer_doc = time.time() - tiempo1

    # Construimos los grumos como árboles
    tiempo1 = time.time()
    bosque.crearGrumos(bosque.conexiones)
    t_lista_grumos = time.time() - tiempo1

    # Selección de grumos
    tiempo1 = time.time()
    grumosSeleccionados = bosque.seleccionarGrumos(porcen)
    if extra =='' :
        salvar_nuevas_relaciones(grumosSeleccionados)
    t_seleccion_grumos = time.time() - tiempo1

    # Total de usuarios y grumos
    [numUsuarios,numGrumos] = bosque.numUsuarios()    # Podría tomarse del documento


    #---MOSTRAR POR PANTALLA RESULTADOS---#

    #   Usuarios conexiones y porcentaje
    print("Número de usuarios ", numUsuarios)
    print("Existen {} grumos.".format( numGrumos ) )
    #   print("Número de usuarios: " + str(len(usr))+". "+"Número de relaciones: "+ str(len(red)) + ".")
    print("Tamaño en porcentaje del mayor grumo deseado: " + str(porcen*100) + "%.")

    #   Tiempos
    print("Duración leer documento: {:.5f} seg.".format(t_leer_doc))
    print("Duración creación lista grumos: {:.5f} seg.".format(t_lista_grumos) )
    print("Duración selección grumos: {:.5f} seg.".format(t_seleccion_grumos) )

    #---RANKING GRUMOS---#
    #   Recuperamos cada uno de los porcentajes de los grumos
    i = 0
    for grumo in grumosSeleccionados:
        i += 1
        print("El grumo {} contiene {} usuarios. Representa un {:.2f}% del total."
        .format (i, grumo[1], grumo[1]/numUsuarios*100 ) )


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




