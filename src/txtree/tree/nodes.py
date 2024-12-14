"""Node that contains the content of a text."""

from __future__ import annotations

import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    """Node that contains the content of a text."""

    id: uuid.UUID
    content: str
    children: list[Node]

    @staticmethod
    def create(content: str) -> Node:
        """Create a new node with the given content."""
        return Node(id=uuid.uuid4(), content=content, children=[])

    def add_child(self, child: Node) -> Node:
        """Add a child node to the current node."""
        self.children.append(child)
        return self

    def __str__(self) -> str:
        return self.content

    def __repr__(self) -> str:
        return f"Node(content='{self.content}'"
