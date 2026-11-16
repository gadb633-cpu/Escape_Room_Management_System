from Helper_functions_and_validations.Handles_JSON import load_from_json,dump_to_json
from Helper_functions_and_validations.inputs import get_num,get_str
from datetime import datetime,timedelta,time

def add_order(path_room,path_order):
    rooms = load_from_json(path_room)
    orders = load_from_json(path_order)
    info_order = get_info_order(orders,rooms)
    new_order = create_order(info_order)
    dump_to_json(path_order,new_order)
    return "Added successfully"

def get_info_order(orders,rooms):
    status_loop= True
    while status_loop:
        order_id = add_order_id(orders)
        customer_name = get_str("enter your name")
        room_id = f"R{get_num("enter room_id"):03d}"
        Number_of_people = get_num("enter Number_of_people")
        room = val_info_order(rooms,room_id,Number_of_people)
        if room == False:
            continue
        while status_loop:
            booking_date = get_str("enter booking_date")
            if check_format_input(booking_date,'%Y-%M-%d') == False:
                continue
            if is_a_future_date(booking_date) == False:
                continue
            start_time = get_str("enter start_time")
            if check_format_input(start_time,'%H:%M') == False:
                continue
            list_time = convert_time(start_time)
            if is_between_the_range(list_time[0]+(list_time[1]/60)) == False:
                continue
            if is_enough_time_before_closing(list_time[0]+(list_time[1]/60),room) == False:
                continue
            if is_have_anther_order(orders,room,room_id,booking_date,list_time) == False:
                continue
            total_price = calculate_price(Number_of_people,room["price_per_player"])
            status_loop = False
    return [order_id,customer_name,room_id,booking_date,start_time,Number_of_people,total_price]

def check_format_input(start_time,format):
    try:
        time = datetime.strptime(start_time,format)
        return True
    except ValueError:
        print(f"only this format {format}")
        return False
    
def convert_time(start_time):
    time = datetime.strptime(start_time,"%H:%M")
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    return [hour,minute]
    
def is_have_anther_order(orders,room,room_id,booking_date,list_time:list):
    correct_min_new_order = (list_time[0]*60)+list_time[1]
    for order in orders:
        if order["room_id"] == room_id:
            if order["booking_date"] == booking_date:
                if order["status"] =="Active":
                    time_order = convert_time(order["start_time"])
                    correct_min_order = (time_order[0]*60)+time_order[1]
                    start = (correct_min_order) - (room["duration"] +15)
                    end = (correct_min_order) + (room["duration"] +15)
                    if start < correct_min_new_order < end:
                        return False
    return True 

def calculate_price(number_of_people,price_per_player): 
    if 1 <= number_of_people <=4 :
        return number_of_people*price_per_player
    elif 5<= number_of_people <=6:
        return (number_of_people*price_per_player) - ((number_of_people*price_per_player)*0.10)
    elif number_of_people >=7:
        return (number_of_people*price_per_player) - ((number_of_people*price_per_player)*0.15)

def is_enough_time_before_closing(hour,room):
    if 22-(room["duration"]/60) >=hour:
        return True
    print("It is not possible to start a game at this time !!")
    return False

def is_between_the_range(hour):
    if 10<=hour <=22:   
        return True
    return False

def is_a_future_date(date):
    this_date = datetime.strptime(date,'%Y-%m-%d')
    now = datetime.today()
    if this_date < now:
        print("the date is in the past")
        return False
    return True

def val_info_order(rooms,room_id,number_of_people):
    room = check_is_room_exist(rooms,room_id)
    if room == False:
        print("room id not found!")
        return False
    elif check_is_available(room) == False:
        print("the room not available !")
        return False
    elif check_num_people(room,number_of_people) == False:
        print("num of people not correct !")
        return False
    return room

def check_is_available(room):
    if room["is_active"] ==True:
        return True
    return False

def check_num_people(room,number_of_people):
    if room["min_players"] <= number_of_people >= room["max_players"]:
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

def create_order(info_order):
    return {
        "booking_id": info_order[0],
        "customer_name": info_order[1],
        "room_id": info_order[2],
        "booking_date": info_order[3],
        "start_time": info_order[4],
        "players": info_order[5],
        "total_price": info_order[6],
        "status": "Active",
        "cancellation_fee": 0.0
    }
# add_order("./db/rooms.json","./db/bookings.json",rooms,orders)