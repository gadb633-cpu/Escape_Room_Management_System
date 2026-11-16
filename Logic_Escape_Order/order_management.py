from display.shaw_orders_menu import shaw_orders_menu
from Helper_functions_and_validations.inputs import get_num,get_str
from display.display_all_items  import display_all_items
from display.display_item import display_item
from Logic_Escape_Order.create_order import add_order
from Logic_Escape_Order.update_order import update_order
def order_management():
    status_loop = True
    while status_loop:
        shaw_orders_menu()
        choice = get_num("enter your choice")
        match choice:
            case 1:
                print(add_order("./db/rooms.json","./db/bookings.json"))
            case 2:
                display_all_items("./db/bookings.json")
            case 3:
                display_item("booking_id","./db/bookings.json")
            case 4:
                display_item("customer_name","./db/bookings.json")
            case 5:
                display_item("booking_date","./db/bookings.json")
            case 6:
                print(update_order("./db/rooms.json","./db/bookings.json"))
            case 7:
                pass
            case 8:
                status_loop = False    
            case _:
                print("choice only between 1-8")