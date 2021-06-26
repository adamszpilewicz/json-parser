from collections import defaultdict
from functools import reduce


def json_restructure(keys: list, record: dict) -> dict:
    structure = {}
    node = structure
    for key in keys[:-1]:
        kv = record[key]
        next_node = node.get(kv, {})
        node[kv] = next_node
        node = next_node
    last_node = node.get(record[keys[-1]], [])
    last_node.append(record["amount"])
    node[record[keys[-1]]] = last_node
    return structure