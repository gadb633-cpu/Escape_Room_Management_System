from Logic_Escape_Room.Handles_JSON import dump_to_json,load_from_json

def display_all_rooms(path):
    data = load_from_json(path)
    for d in data:
        print("\n")
        for key,value in d.items():
            print(f"{key},{value}")
            