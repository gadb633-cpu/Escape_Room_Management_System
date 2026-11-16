from Helper_functions_and_validations.Handles_JSON import load_from_json,dump_to_json
from Helper_functions_and_validations.inputs import get_num

def add_order(path_room,path_order):
    orders = load_from_json(path_order)
    info_room = get_info_order(orders)
    new_order = create_order(info_room)
    dump_to_json(path_order,new_order)
    return "Added successfully"

def get_info_order(orders,rooms):
    status_loop= True
    while status_loop:
        order_id = add_order_id(orders)
        room_id = f"R{get_num("enter room_id"):03d}"
        Number_of_people = get_num("enter Number_of_people")
        if val_info_order(rooms,room_id) == False:
            continue
        

def val_info_order(rooms,room_id):
    room = check_is_room_exist(rooms,room_id)
    if room == False:
        print("room id not found!")
        return False
    elif check_is_available(room) == False:
        print("the room not available !")
        return False
    elif check_num_people(room) == False:
        print("num of people not correct !")
        return False
    return True

def check_is_available(room):
    if room["is_active"] ==True:
        return True
    return False

def check_num_people(room,number_of_people):
    if room["min_players"] <= number_of_people <=room["max_players"]:
        return True
    return False

def check_is_room_exist(rooms,room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room
    return  False
    
def add_order_id(orders):
    order_id = len(orders) + 1
    return f"B{order_id:03d}"

def create_order(info_room):
    pass