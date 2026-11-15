from Logic_Escape_Room.Handles_JSON import dump_to_json,load_from_json
from Helper_functions_and_validations.inputs import get_num,get_str
from display.display_result import display_result

def display_item(type_,path):
    items = []
    if type_ == "booking_date":
        item = get_date_to_search()
    elif type_ == "customer_name":
        item = get_name_to_search()
    else:    
        item = get_id_to_search(type_)
    data = load_from_json(path)
    for d in data:
        if item == d[type_]:
            items.append(d)
    if items ==[]:
        print("not found!!")
        return        
    display_result(items)

def get_id_to_search(type_):
    num_id = get_num("enter item id")
    if type_ == "booking_id":
        return f"B{num_id:03d}"
    elif type_ == "room_id":
        return f"R{num_id:03d}"
    
def get_name_to_search():  
    name = get_str("enter customer_name")
    return name

def get_date_to_search():
    date = get_str("enter booking_date (example: 2026-11-14)")
    return date