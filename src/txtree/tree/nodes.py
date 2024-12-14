"""Node that contains the content of a text."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    """Node that contains the content of a text."""

    content: str

    @staticmethod
    def create(content: str) -> Node:
        """Create a new node with the given content."""
        return Node(content=content)

    def __str__(self) -> str:
        return self.content

    def __repr__(self) -> str:
        return f"Node(content='{self.content}'"
