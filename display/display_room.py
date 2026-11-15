from Logic_Escape_Room.Handles_JSON import dump_to_json,load_from_json

def display_room(room_id,path):
    data = load_from_json(path)
    for d in data:
        if room_id == d["room_id"]:
            for key,value in d.items():
                print(key,value)
            return    
    print("not found!!")
    return