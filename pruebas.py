import treap_structure as treap

tree = treap.GrumoTreap()
tree.___init__()
tree.addRelacion(1,5)
tree.addRelacion(5,10)
tree.addRelacion(10,15)
tree.addRelacion(10,25)
tree.addRelacion(4,3)
tree.addRelacion(2,8)
print(tree.representarEnCascada(tree.hijos))
