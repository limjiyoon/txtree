from txtree.tree.tree import Tree


def test_add_node():
    tree = Tree()
    node1 = tree.add_node("node1")
    node2 = tree.add_node("node2")
    tree.add_edge(tree.root, node1)
    tree.add_edge(node1, node2)
