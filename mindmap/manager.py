from mindmap.models import MindMap, Node


def create_mind_map(title: str):
    map = MindMap()
    map.title = title
    return map


# def add_node(node: Node, name: str, path: str):
#     if len(node.children) != 3:
#         parts = [part.strip() for part in path.split(">")]
#         current = node[0]
#         for part in parts:
#             found = False
#             for child in current.children:
#                 if child.name == part:
#                     current = child
#                     found = True
#                     break
#             if not found:
#                 print(f"Node '{part}' not found under '{current.name}'!")
#                 return False
#         new_node = Node(name, [])
#         current.children.append(new_node)
#         print(f"✅ Node '{name}' added under '{current.name}'")
#         return True
#     else:
#         print(f"❗This node already have 3 children")


def serach_node(node: Node, title):
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

