from mindmap.models import Node


def create_mind_map(title: str):
    map = Node(title, [])
    map.title = title
    return map



def search_node(node: Node, title, path=''):
    if node.name == title:
        return path
    else:
        path += ' > ' + node.name

    for child in node.children:
        result = search_node(child, title, path)
        if result:
            return result


def delete_node(node: Node, name: str):
    index = next((index for (index, d) in enumerate(node.children) if d.name == name), None)
    if index is not None:
        del node.children[index]
        return node.children
    else:
        return None


def list_nodes(node, prefix: str):
    print(prefix + node.name)
    for idx, child in enumerate(node.children):
        is_last = idx == len(node.children) - 1
        child_prefix = prefix + ("  ")
        branch_symbol = " └─ " if is_last else " ├─ "
        print(prefix + branch_symbol, end="")
        list_nodes(child, child_prefix)


def edit_node(node: Node, name_to_edit: str):
    new_name = input("Write the name you want to replace with : ").strip()
    index = next((index for (index, n) in enumerate(node.children) if n.name == name_to_edit), None)
    if index is not None:
        node.children[index].name = new_name
        return node
    else:
        print("❗ Couldn't found any node with this name")
