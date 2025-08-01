#QUESTION

"""
Task 6: Electronics Store Nested Cart
Three friends, Tobi, Lami, and Chinedu, visit an electronics store together. 
They decide to share **one big smart cart** that can group items by the department they are picked from.
The cart keeps track of each department with the items selected inside it.

cart = {
    "phones": {},
    "laptops": {},
    "accessories": {}
}

Each product in the store is represented as a tuple: (product_name, price) because these details never change.

During shopping:
- Tobi picks up an iPhone for 750000 Naira in the "phones" department.
- Lami adds a Dell XPS Laptop for 1200000 Naira in the "laptops" department.
- Chinedu adds Wireless Earbuds for 50000 Naira in the "accessories" department.
- Tobi changes his mind and removes the iPhone from the cart.
- Lami then adds another accessory: a Gaming Mouse for 35000 Naira.

At checkout:
- A snapshot of the nested cart is taken as the order summary for the store record.
- The shared smart cart is then completely emptied to reset for the next customers.
"""


# SOLUTION


cart = {
    "phones": {},
    "laptops": {},
    "accessories": {}
}

tobi = cart
lami = cart
chinedu = cart

# Add items
tobi["phones"].update({"iPhone": 750000})
lami["laptops"].update({"Dell XPS": 1200000})
chinedu["accessories"].update({"Earbuds": 50000})

# Tobi removes only iPhone, not whole 'phones'
tobi["phones"].pop("iPhone")

# Lami adds another accessory
lami["accessories"].update({"Gaming Mouse": 35000})

# Take snapshot
order_summary = cart.copy()

# Reset cart
cart.clear()

print("Snapshot:", order_summary)
print("Cart after clearing:", cart)

