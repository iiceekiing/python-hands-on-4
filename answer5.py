"""
Task 5: Online Shopping Cart
Two friends, Daniella and Godiya, walk into a mall and pick up just one cart to shop with.
Once inside, they split up and go to different wings of the mall, 
but since they share the same cart, everything either of them adds goes into the same cart.

cart = {}
the final ordergodiya = ???
daniella = ???

During shopping:
- Daniella finds and adds "Shoes" (2 quantity).
- Godiya picks up "Watch" (1 quantity).
- Daniella later changes her mind and removes "Shoes" from the cart.
- Godiya also adds a "Bag" (1 quantity), then later removes it.

At checkout:
- The store takes a snapshot of the final order as an order summary for records.
- The shared cathe final orderrt is then emptied to prepare it for the next customer.
"""


cart = {}


daniella = cart
godiya = cart

#Daniella finds and adds "Shoes" (2 quantity).
daniella.update({"Shoes": 2,})

#Godiya picks up "Watch" (1 quantity).
godiya.update({"Watch": 1,})

"""
print(id(cart))
print(id(godiya))
print(id(daniella))
#Daniella later changes her mind and removes "Shoes" from the cart.
#daniella.pop("Shoes")
"""


#Godiya also adds a "Bag" (1 quantity). then later removes it.
godiya.update({"Bag": 1})

#then later removes it (The bag she added recently). 
godiya.popitem()
#or 
#godiya.pop(bag)

#cart.update(godiya)
#print(cart)

#cart.update(daniella)

print(cart)

print("snapshot of The final order: ", cart)

cart.clear()
print(cart)



print(godiya)
print(daniella)
print(godiya == daniella) # should return true
print(cart)
