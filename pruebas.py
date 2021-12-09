# import treap_structure as treap

# tree = treap.GrumoTreap()
# primerHijo = treap.Usuario(0)
# otroHijo = treap.Usuario(19)
# primerHijo.hijoMayor = otroHijo
# tree.___init__(primerHijo)
# tree.addRelacion(6,2)
# tree.addRelacion(2,4)
# tree.addRelacion(5,3)
# tree.addRelacion(3,7)
# tree.addRelacion(7,4)
# tree.addRelacion(2,1)
# print("###########################")
# for hijo in tree.hijos:
#     print(tree.representarEnCascada(hijo))

# import treap_structure_final as treap

# bosque = treap.Bosque()
# bosque.___init__()
# for parejaNumero in [(5,2),(10,3),(21,15),(4,2),(5,7),(8,10),(8,4)]:
#     bosque.addConexion(parejaNumero[0],parejaNumero[1])
# bosque.crearGrumos(bosque.conexiones)
# bosque.representarGrumos()
# i = 0
# for porcentaje in bosque.obtenerPorcentajes():
#     i += 1
#     print("El porcentaje del grumo {} es {:.2f}".format(i,porcentaje))

def addGrumo(grumo,grumos,lista,pos=0):
        print(lista,pos)
        # Si se ha acabado la lista metemos nuestro grumo
        if len(lista)==0:
            grumos.insert(pos,grumo)
            return

        # Determinamos la mediana para comparar
        
        mitad = len(lista)//2
        mediana = lista[mitad][1]
        if len(lista)%2==0:
            mediana = (mediana + lista[mitad-1][1])/2

        # Elegimos a cual de las dos mitades pertenece nuestro nuevo grumo
        if mediana < grumo[1]:
            addGrumo(grumo,grumos,lista[:mitad],pos)
            return
        # Incrementamos la posición  
        pos += mitad + 1
        if mediana > grumo[1]:
            # Si pertenece a la segunda mitad sumamos la posición
            
            addGrumo(grumo,grumos,lista[mitad+1:],pos)
            return
        else:
            addGrumo(grumo,grumos,[],pos)
            return

array = [[5,5],[4,4],[3,3],[2,2]]

grumos = [[2,2],[6,7],[4,5],[7,9],[3,8]]
for grumo in grumos:
    addGrumo(grumo,array,array)
    print(array)