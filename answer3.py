"""
Task 3: Hotel Room Allocation
Hill View Hotel tracked room occupancy as follows:

rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

During the evening:
- A new guest "Daisy" was checked into room 104.
- Room 102 was vacated after Bob checked out.
- A last-minute cancellation happened for the most recently allocated room just after the manager backed up the current allocation.
"""


rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

pre_record = rooms.copy()

#print(pre_record)

rooms["104"] = "Daisy"

rooms.pop("102")

rooms.pop("104")

post_record = rooms.copy()

#print(post_record)

print("Previous room allocation record:", pre_record)

print("Updated room allocation record:", rooms)


