import treap_structure as treap

tree = treap.GrumoTreap()
primerHijo = treap.Usuario(0)
tree.___init__(primerHijo)
tree.addRelacion(6,2)
tree.addRelacion(2,3)
tree.addRelacion(8,5)
tree.addRelacion(2,5)
tree.addRelacion(5,9)
tree.addRelacion(7,5)
print("---------------------")
for hijo in tree.hijos:
    print(tree.representarEnCascada(hijo,0))