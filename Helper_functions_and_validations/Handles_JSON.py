import json

def load_from_json(path):
    try:
        with open(path,"r", encoding="utf-8") as file:
            data = file.read()
            data = json.loads(data)
            return data
    except FileNotFoundError:
        return []
    
def dump_to_json(path,new_item):
    data = load_from_json(path)
    data.append(new_item)
    with open(path, "w") as file:
        data2 = json.dumps(data,indent=4)
        file.write(data2)

def update_json(path,list_items):
    with open(path, "w") as file:
        data = json.dumps(list_items,indent=4)
        file.write(data)