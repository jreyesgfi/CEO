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

import treap_structure_final as treap

bosque = treap.Bosque()
bosque.___init__()
for parejaNumero in [(5,2),(10,3),(21,15),(4,2),(5,7),(8,10)]:
    bosque.addConexion(parejaNumero[0],parejaNumero[1])
bosque.crearGrumos(bosque.conexiones)
print(bosque.representarGrumos())