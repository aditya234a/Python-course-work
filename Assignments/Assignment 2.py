print("Magicpin Food Delivery Details".center(50,"*"))

booking_id = input("Enter the Booking id:")
item_name = input("enter the Item Name: ")
item_price = float(input("enter the Item Price: "))
discount_price = float(input("enter the Discount Value: "))
delivery_distance = float(input("Enter the Distance: "))
delivery_charges = int(input("Enter the Delivery Charges : "))
delivery_person_name= input("Enter the delivery person name: ")
delivery_contact_details = int(input("Enter the contact number: "))
delivery_location = input("Enter the Delivery Location:")

total_price = item_price - discount_price + delivery_charges 



print("Booking id: ",booking_id, "\nItem : ", item_name,"\nPrice : ", item_price)

print("Discount %2f" %(discount_price) + "%")

print(f'Distance : {delivery_distance} km \nDelivery Charges : {delivery_charges} \nPerson Name :{delivery_person_name}')

print("Contact Number : +91 {} \nLocation : {}".format(delivery_contact_details, delivery_location))

print(f'Total Price : Rs.{total_price}')

