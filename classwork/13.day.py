
print("Welcome to Grocery Store".center(50,'-'))
grocery_products ={
                    1:{"product": "sugar", "price": 40},
                    2:{"product":"cooking oil", "price":120},
                    3:{"product":"tea powder", "price":50},
                    4:{"product":"bread", "price":30},
                    5:{"product":"soap", "price":25}
}
for i in grocery_products:
    print(f'{i}.{grocery_products[i]["product"]} -  {grocery_products[i]["price"]} ')

items = list(map(int,input("enter the grocery_products(1 2 3 4 5):").split()))

total = 0
s = set()
for i in items:
    if i not in s:
        c = items.count(i)
        print(f'{grocery_products[i]  ["product"]} - {c}  *  {grocery_products[i]["price"]} = {c*grocery_products[i]["price"]}')
        total+=grocery_products[i]  ["price"]  *  c
        s.add(i)
print(f"total bills:{total}")







