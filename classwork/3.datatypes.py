a = 10
print(type(a))       #integer

a = 10.0
print(type(a))       #float

a = 3+3j
print(type(a))       #comlpex

name = 'aditya'
print(type(name))    #string

cart_items = ["shoes","T-shirts","headphones"]
print(type(cart_items))                      #list

warehouse_location = (12.9716, 77.5946)
print(type(warehouse_location))           #tuple

available_sizes = {"s","d","c"}
print(type(available_sizes))                #set

frozen_tags = frozenset(["sale","trending"])
print(type(frozen_tags))                    #frozenset

product_details ={
    "name": "wireless mouse",
    "brand": "asus",
    "price": 699
}
print(type(product_details))               #dictionary

logged_in = True
payment_successful = False
in_stock = True
print(type(in_stock))                    #boolean

tracking_number = None
delivery_partner = None
print(type(tracking_number))              #nonetype
 