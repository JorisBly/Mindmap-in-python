
class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children if children is not None else []

    @staticmethod
    def from_dict(data):
        node = Node(data["name"], data["children"])
        node.children = [Node.from_dict(child) for child in data.get("children", [])]
        return node
