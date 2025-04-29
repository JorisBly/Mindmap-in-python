import os

import yaml

from mindmap.models import  Node

def to_dict(node: Node):
    return {
        "name": node.name,
        "children": [to_dict(child) for child in node.children]
    }

def save_mindmap(root_node: Node,filename: str):
    if '.yml' not in filename:
        filename += '.yml'


    with open(get_filepath(filename), "w") as f:
        yaml.dump(to_dict(root_node), f, allow_unicode=True)

def load_mindmap(filename: str):
    if '.yml' not in filename:
        filename += '.yml'
    with open(get_filepath(filename), "r") as f:
        data = yaml.safe_load(f)
        return Node.from_dict(data)


def get_filepath(filename:str):
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    full_path = os.path.join(data_dir, filename)
    return full_path