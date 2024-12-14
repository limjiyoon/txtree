"""Tree class manage the relationship among nodes."""

from __future__ import annotations

from collections import defaultdict

from src.txtree.tree.nodes import Node


class Tree:
    """Tree class manage the relationship among nodes."""

    def __init__(self):
        self._root = Node.create("")
        self._nodes = {self._root}
        self._adj = defaultdict(list)

    def add_node(self, content: str) -> Node:
        """Add a new node with the given content."""
        node = Node.create(content)
        self._nodes.add(node)
        return node

    def add_edge(self, src: Node, dst: Node) -> None:
        """Add an edge between the given nodes."""
        self._adj[src].append(dst)

    @property
    def root(self) -> Node:
        """Return the root node of the tree."""
        return self._root
