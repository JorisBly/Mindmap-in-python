from mindmap.models import Node


def create_mind_map(title: str):
    map = Node(title, [])
    map.title = title
    return map



def search_node(node: Node, title):
    for children in node.children:
        path = None
        for node in children:
            path += node.title + '>'
        if path is not None and title in path:
            return path
        else:
            return 'Sorry no node founded'


def list_nodes(node, prefix: str):
    print(prefix + node["name"])
    children = node.get("children", [])
    for idx, child in enumerate(children):
        is_last = idx == len(children) - 1
        child_prefix = prefix + ("    " if is_last else "│   ")
        branch_symbol = "└─ " if is_last else "├─ "
        print(prefix + branch_symbol, end="")
        list_nodes(child, child_prefix)


def delete_node(node: Node):
    return

