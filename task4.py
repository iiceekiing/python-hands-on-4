"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)


participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

print("\n First Record: ", participants)
participants.update({"Guest": "Daisy"})

print("\n Ticket record after adding the 'Guest' ticket:  ", participants)

#participants_snapshot = participants.copy()

#record_before_pop = participants_snapshot.copy()

participants.pop("Student")
print('\n Record After The "Student" participant canceled their registration', participants)

record_before_removing_last  = participants.copy()

print("\n record for the day before removing the most recently added participant: ", record_before_removing_last)

#last_remove = participants.popitem()
participants.popitem()

print("\n Ticket Record After Removing The Most Recently Added Participant: ", participants)
