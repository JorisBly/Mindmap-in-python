
class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children


class MindMap:
    def __init__(self, name):
        self.title = name
        self.children = []
    title: str = ''
    nodes: list[Node] = []