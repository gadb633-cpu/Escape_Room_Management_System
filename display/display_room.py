from Logic_Escape_Room.Handles_JSON import dump_to_json,load_from_json
from Helper_functions_and_validations.inputs import get_num,get_str
def display_room(id,path):
    data = load_from_json(path)
    for d in data:
        if id == d["room_id"]:
            for key,value in d.items():
                print(key,value)
            return    
    print("not found!!")
    return

def get_id_to_search():
    num_id = get_num("enter room id")
    return f"R{num_id:03d}"