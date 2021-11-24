import treap_structure as treap

tree = treap.GrumoTreap()
primerHijo = treap.Usuario(0)
tree.___init__(primerHijo)
tree.addRelacion(6,2)
tree.addRelacion(2,4)
tree.addRelacion(5,3)
tree.addRelacion(3,7)
tree.addRelacion(7,4)
print("---------------------")
i=0
for hijo in tree.hijos:
    i += 1
    print(hijo.id)
    #print(tree.representarEnCascada(hijo,0))