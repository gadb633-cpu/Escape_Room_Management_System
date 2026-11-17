
def display_result(items):
    for item in items:
        print("\n")
        for key,value in item.items():
            print(f"{key}: {value}")
