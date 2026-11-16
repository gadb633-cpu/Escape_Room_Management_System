from Helper_functions_and_validations.inputs import get_num,get_str
from Logic_Escape_Order.create_order import *
from Helper_functions_and_validations.Handles_JSON import load_from_json,update_json

def update_order(path_rooms,path_orders):
    rooms = load_from_json(path_rooms)
    orders = load_from_json(path_orders)
    booking_id = f"B{get_num("enter booking_id,(enter only num)"):03d}"
    the_order = get_order(orders,booking_id)
    the_room = get_room(rooms,the_order["room_id"])
    list_new_item = choice_update(the_order,the_room,orders)
    the_order[list_new_item[0]]= list_new_item[1]
    the_order["total_price"] = list_new_item[2]
    update_json(path_orders,orders)
    return "Updated successfully!"

def get_room(rooms,room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room
    print("not found")
    return    

def get_order(orders,booking_id):
    for order in orders:
        if order["booking_id"] == booking_id:
            return order
    print("not found")
    return
    
def choice_update(the_order,the_room,orders):
    status_loop = True
    while status_loop:
        choice = get_str("enter your choice [booking_date,start_time,players]")
        match choice:
            case "booking_date":
                booking_date = get_str("enter new booking_date")
                day = check_day(booking_date)
                if check_format_input(booking_date,'%Y-%M-%d') == False:
                    continue
                if is_a_future_date(booking_date) == False:
                    continue
                total_price = calculate_price(the_order["players"],the_room["price_per_player"],day)
                return [choice,booking_date,total_price]
            case "start_time":
                start_time = get_str("enter start_time")
                if check_format_input(start_time,'%H:%M') == False:
                    continue
                list_time = convert_time(start_time)
                if is_between_the_range(list_time[0]+(list_time[1]/60)) == False:
                    continue
                if is_enough_time_before_closing(list_time[0]+(list_time[1]/60),the_room) == False:
                    continue
                if is_have_anther_order(orders,the_room,the_order["room_id"],booking_date,list_time) == False:
                    continue
                return [choice,start_time,the_order["total_price"]]
            case "players":
                players = get_num("enter players")
                if check_num_people(the_room,players) == False:
                    continue
                total_price = calculate_price(players,the_room["price_per_player"],check_day(the_order["booking_date"]))
                return [choice,players,total_price]
            case _:
                print("only in [booking_date,start_time,players] !!!")
