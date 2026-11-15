from Helper_functions_and_validations.inputs import get_num,get_str
from Logic_Escape_Room.Handles_JSON import load_from_json,dump_to_json

def add_room(path):
    rooms = load_from_json(path)
    info_room = get_info_room(rooms)
    new_room = create_room(info_room)
    dump_to_json(path,new_room)
    print("ok")

def create_room(info_room):
    return {
        "room_id": info_room[0],
        "name": info_room[1],
        "difficulty": info_room[2],
        "duration": info_room[3],
        "min_players": info_room[4],
        "max_players": info_room[5],
        "price_per_player": info_room[6],
        "is_active": True
        }

def get_info_room(rooms):
    status_loop = True
    while status_loop:
        room_id = add_id(rooms)
        name = get_str("enter name room")
        difficulty = check_difficulty()
        duration = get_num("enter duration")
        min_players = get_num("enter min_players")
        max_players = get_num("enter max_players")
        price_per_player = get_num("enter price_per_player")
        return [room_id,name,difficulty,duration,min_players,max_players,price_per_player]
    
def check_difficulty():
    status_loop = True
    while status_loop:
        difficulty = get_str("enter difficulty [Easy,Medium,Hard]")
        if difficulty.lower() in ["easy","medium","hard"]:
            status_loop = False
            return difficulty
        print("only [Easy,Medium,Hard] !!!")
        
def add_id(rooms:list):
    num_id = len(rooms) +1
    return f"R{num_id:03d}"