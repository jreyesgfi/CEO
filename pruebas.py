import treap_structure as treap

tree = treap.GrumoTreap()
tree.___init__()
tree.addRelacion(1,2)
tree.addRelacion(3,4)
tree.addRelacion(5,6)
tree.addRelacion(2,7)
tree.addRelacion(3,8)
print(tree.representarEnCascada(tree.arbol))