from Helper_functions_and_validations.inputs import get_str,get_num
from Logic_Escape_Order.create_order import convert_time
from datetime import datetime
from Helper_functions_and_validations.Handles_JSON import load_from_json,update_json
from Logic_Escape_Order.update_order import get_order

def cancel_order(path_orders):
    orders = load_from_json(path_orders)
    booking_id = f"B{get_num("enter booking_id,(enter only num)"):03d}"
    the_order = get_order(orders,booking_id)
    if the_order["status"] == "Cancelled":
        return "it's already Cancelled!"
    discount_price = check_time_left([the_order["booking_date"],the_order["start_time"]])
    cancellation_fee = calculate_cancel_price(the_order["total_price"],discount_price)
    the_order["cancellation_fee"] = cancellation_fee
    the_order["status"] = "Cancelled"
    update_json(path_orders,orders)
    return "Cancelled successfully!"


def calculate_cancel_price(total_price,percent):
    if percent == 0:
        return 0
    elif percent == 25:
        return total_price /4
    elif percent == 50:
        return total_price /2

def check_time_left(time_order:list):
    day_order = convert_dates(time_order[0])
    now = datetime.today()
    day_now = int(now.strftime("%d"))
    hour_now = now.strftime("%H:%M")
    list_time = convert_time(time_order[1])
    now_list_time = convert_time(hour_now)
    if day_now + 1 == day_order:
        if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) > 24*60:
            return 0
        if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) >= 6*60:
            return 25
        if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) < 6*60:
            return 50
    if day_now == day_order:
        if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) >= 6*60:
            return 25
        if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) < 6*60:
            return 50
    return 0
    
def convert_dates(date):
    convert_date = datetime.strptime(date,'%Y-%M-%d')
    day = int(convert_date.strftime("%d"))
    return day