from mindmap.models import MindMap, Node


def create_mind_map(title:str):
    map = MindMap()
    map.title = title
    return map

def add_node(node: Node, name: str, path: str):
    parts = [part.strip() for part in path.split(">")]
    current = node.nodes[0]
    for part in parts:
        found = False
        for child in current.children:
            if child.name == part:
                current = child
                found = True
                break
        if not found:
            print(f"Node '{part}' not found under '{current.name}'!")
            return False
    new_node = Node(name, [])
    current.children.append(new_node)
    print(f"✅ Node '{name}' added under '{current.name}'")
    return True

def serach_node(node: Node, title):
    for children in node.children:
        path = None
        for node in children:
            path += node.title +'>'
        if path is not None and title in path:
             return path
        else:
            return 'Sorry no node founded'

def list_nodes(node, prefix:str):
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

# def add_node(mindmap: MindMap, Node: Node, new_name):
#     node = find_node(mindmap.root, path)
#     if node and depth(node) < 2:
#         node.children.append(Node(new_name))
#         return True
#     return False
#
# def delete_node(mindmap, path):
#     parent_path, node_name = path[:-1], path[-1]
#     parent = find_node(mindmap.root, parent_path)
#     if parent:
#         parent.children = [child for child in parent.children if child.name != node_name]
#         return True
#     return False
#
# def list_nodes(node, prefix=""):
#     print(prefix + node.name)
#     for child in node.children:
#         list_nodes(child, prefix + "  ")
#
# def find_node(node: Node, path):
#     for part in path:
#         node = next((child for child in node.children if child.name == part), None)
#         if node is None:
#             break
#     return node
#
# def depth(node):
#     return 0 if not node.children else 1 + max(depth(child) for child in node.children)
