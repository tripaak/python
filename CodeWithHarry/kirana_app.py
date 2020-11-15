#Author : Akash Tripathi
#Date: 12-11-2020

items_dict = {}

def total_bill_calculation(some_dict):
    total = 0
    print(f"{'Items'}: {'Price'}")
    for key, value in some_dict.items():
        print(f"{key}: {value}")
        total = total + int(value)
    items_dict['total bill'] = total
    print(f"total : {total}") 
    items_dict.clear()   
    # print(items_dict)





while True:
    try:
        item,price = input("Enter the item and price, comma separted: ").split(',')
        items_dict[item] = int(price)
    except KeyboardInterrupt:
        print("Printing Bill.............")    
        break


total_bill_calculation(items_dict)

