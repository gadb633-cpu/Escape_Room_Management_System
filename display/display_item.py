from Logic_Escape_Room.Handles_JSON import dump_to_json,load_from_json
from Helper_functions_and_validations.inputs import get_num

def display_item(type_id,path):
    item_id = get_id_to_search(type_id)
    data = load_from_json(path)
    for d in data:
        if item_id == d[type_id]:
            for key,value in d.items():
                print(key,value)
            return    
    print("not found!!")
    return

def get_id_to_search(type_id):
    num_id = get_num("enter room id")
    if type_id == "booking_id":
        return f"B{num_id:03d}"
    elif type_id == "room_id":
        return f"R{num_id:03d}"