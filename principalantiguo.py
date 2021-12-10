import time

#Definimos nuestras listas y valores globales


#Empezamos leyendo las líneas del documento una a una
def leer_relaciones(fprin, fextra):

    # Número de usuarios
    n = 0
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
                m = int(linea)
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
                #Definimos una nueva relación
                nr=[]
                for palabra in linea.split():
                    nr.append(int(palabra))
                    '''try:
                       nr.append(int(palabra))
                    except:
                        print("La relación de una pareja de elementos es incorrecta")'''
                if (len(nr)==2): #Esta comprobación se podría quitar pues supnemos que es correcta
                    red.append(nr)
            l = l + 1


    if fextra != "":
        with open(fextra) as f:
            for linea in f:
                nr = []
                for palabra in linea.split():
                    nr.append(int(palabra))
                    '''try:
                        nr.append(int(palabra))
                    except:
                        print("La relación de una pareja de elementos es incorrecta")'''
                if (len(nr) == 2):
                    red.append(nr)
    return (red)

    # Creamos la lista de usuarios
def lista_usuarios(red):
    usr = []
    for r in red:
        for p in r:
            if p not in usr:
                usr.append(p)
    return (usr)

    # Definimos la función que construye un grumo nuevo
def uber_amigos(ui, red, grumo):
    grumo.append(ui)
    for r in red:
        if r[0] == ui and r[1] not in grumo:
            uber_amigos(r[1], red, grumo)
        elif r[1] == ui and r[0] not in grumo:
            uber_amigos(r[0], red, grumo)


def estructura_grumos(usr,red):
    # Individuos que ya pertencen a un grupo
    asig = []
    # Lista de los grumos ya existentes
    grus = []
    #Recorremos todos los elementos creando grumos si no poseen uno
    for p in usr:
        if p not in asig:
            grumo=[]
            uber_amigos(p,red,grumo)
            grus.append(grumo)
            for i in grumo:
                asig.append(i)
    return (grus)

def ordenacion_grumos(grus):
    grus = sorted(grus, key = len, reverse=True)
    return grus

def seleccion_grumos(grus,usr,porcen):
    n = len(usr)
    grumoP = None
    f = open("extra.txt","w") #De esta forma se borra automáticamente el anterior extra.txt
    i = 0
    for grumo in grus:
        i += 1
        #Escribimos el grumo y su porcentaje
        #("#"+str(i)+":  "+str(len(grumo))+" usuarios"+"  ("+str(len(grumo)/n*100)+")print%")

        #Comprobamos que no estamos en el primer grupo
        if grumoP != None:
            #Creamos la nueva relación
            f.write(str(grumoP[0])+" "+str(grumo[1])+"\n")
            #print("Recomendación de unión: Usuario "+str(grumoP[0])+" con usuario:"+str(grumo[1]))

        #Quitamos el porcentaje de usuarios que pertenecen al grumo
        porcen = porcen - (len(grumo)/n)

        #Comprobamos si ya hemos cubierto el porcentaje
        if porcen <= 0:
            f.close()
            return (i)
        else:
            #Almacenamos el anterior grupo para crear la siguiente relación
            grumoP = grumo
def main():
    # Preguntar fichero a abrir y porcentaje
    principal = input("Introduzca el nombre del fichero principal.")
    extra = input("Introduzca el nombre del fichero extra o pulse ENTER.")
    porcen = float(input("Introduzca el porcentaje deseado")) / 100

    # Leemos el documento y creamos la lista de redes
    tiempo1 = time.time()
    red = leer_relaciones(principal, extra)
    t_leer_doc = time.time() - tiempo1

    # Construimos la lista de usurarios y de redes
    tiempo1 = time.time()
    usr = lista_usuarios(red)
    t_lista_usuarios = time.time() - tiempo1

    # Obtenemos la lista de grumos
    tiempo1=time.time()
    grus = estructura_grumos(usr,red)
    t_lista_grumos = time.time() - tiempo1

    # Ordenamos los grumos por tamaño
    tiempo1 = time.time()
    grus = ordenacion_grumos(grus)

    # Selección de grumos
    grus_picked = seleccion_grumos(grus,usr,porcen)
    t_ordenar_grumos = time.time() - tiempo1

    # Mostrar por pantalla resultados

    #Usuarios conexiones y porcentaje
    print("Número de usuarios: " + str(len(usr))+". "+"Número de relaciones: "+ str(len(red)) + ".")
    print("Tamaño en porcentaje del mayor grumo deseado: " + str(porcen*100) + "%.")

    #Tiempos
    print("Duración leer documento: {:.5f} seg.".format(t_leer_doc))
    print("Duración creación lista de usuarios: {:.5f} seg.".format(t_lista_usuarios) )
    print("Duración creación lista grumos: {:.5f} seg.".format(t_lista_grumos) )
    print("Duración ordenación y seleección de grumos: {:.5f} seg.".format(t_ordenar_grumos) )

    #Ranking grumos
    print("Existen {} grumos.".format(len(grus)))
    print("Se deben unir los {} mayores.".format(grus_picked))
    for i in range(grus_picked):
        print("#{}: {} usuarios, ({:.2f}%).".format(i+1, len(grus[i]), len(grus[i]) / len(usr)* 100) )

    #Recomendaciones de uniones
    if grus_picked !=1:
        print("Las nuevas relaciones de amistad (salvadas en extra.txt) son:")
        with open("extra.txt") as f:
            for linea in f:
                print("{} con {}.".format(linea.split()[0],linea.split()[1]))
    else:
        print("No hacen falta nuevas relaciones de amistad.")
main()




