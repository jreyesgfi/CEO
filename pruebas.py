import treap_structure as treap

tree = treap.GrumoTreap()
tree.___init__()
tree.addRelacion(4,7)
tree.addRelacion(7,3)
tree.addRelacion(7,2)
tree.addRelacion(3,15)
print(tree.representarEnCascada(tree.hijos))
