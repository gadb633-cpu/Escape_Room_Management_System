import json

def load_from_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.loads(file)

def dump_to_json(path,new_item):
    data = load_from_json(path)
    data.append(new_item)
    with open(path, "w", encoding="utf-8") as file:
        json.dumps(data, file, indent=4, ensure_ascii=False)
