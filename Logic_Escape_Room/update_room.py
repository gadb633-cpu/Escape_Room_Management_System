from Helper_functions_and_validations.inputs import get_num,get_str
from Helper_functions_and_validations.Handles_JSON import load_from_json,update_json
from Logic_Escape_Room.add_room import check_difficulty

def update_room(path):
    num1 = get_num("enter room id,(enter only num)")
    room_id = f"R{num1:03d}"
    data_to_change = choice_update()
    rooms = load_from_json(path)
    for room in rooms:
        if room_id == room["room_id"]:
            room[data_to_change[0]] = data_to_change[1]
            update_json(path,rooms)
            return "Updated successfully!"
    return "not found!!"     

def choice_update():
    status_loop = True
    while status_loop:
        choice = get_str("enter your choice [name,difficulty,duration,min_players,max_players,price_per_player]")    
        match choice:
            case "name":
                name = get_str("enter new name")
                return [choice,name]
            case "difficulty":
                difficulty = check_difficulty()
                return [choice,difficulty]
            case "duration":
                duration = get_num("enter new duration")
                return [choice,duration]
            case "min_players":
                min_players = get_num("enter new min_players")
                return [choice,min_players]
            case "max_players":
                max_players = get_num("enter new max_players")
                return [choice,max_players]
            case "price_per_player":
                price_per_player = get_num("enter new price_per_player")
                return [choice,price_per_player]
            case _:
                print("only in [name,difficulty,duration,min_players,max_players,price_per_player] !!!")

def update_is_active(path):
    num1 = get_num("enter room id, (enter only num)")
    room_id = f"R{num1:03d}"
    is_active = check_is_active()
    rooms = load_from_json(path)
    for room in rooms:
        if room_id == room["room_id"]:
            room["is_active"] = is_active
            update_json(path,rooms)
            return "Updated successfully!"
    return "not found!!"

def check_is_active():
    status_loop = True
    while status_loop:
        is_active = get_str("enter 1[true] or 0[false]")
        if is_active == "1":
            status_loop = False
            return True
        elif is_active =="0":
            status_loop = False
            return False
        print("only 1 or 0")