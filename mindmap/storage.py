import yaml

from mindmap.models import  Node

def to_dict(node: Node):
    return {
        "name": node.name,
        "children": [to_dict(child) for child in node.children]
    }

def save_mindmap(root_node: Node,filename: str):
    with open(filename, "w") as f:
        yaml.dump(to_dict(root_node), f, allow_unicode=True)

def load_mindmap(filename: str):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
        node = Node(data['name'], [])
        node.children = [Node(child['name'], child['children']) for child in data.get("children", [])]
        return node

