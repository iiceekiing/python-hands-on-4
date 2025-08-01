"""
Task 2: Airport Luggage Tracker
At Jos Airport, the luggage department tracked passengers and their luggage weights:

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

- you need to map each user to its corresponding luggage weight value.

Before the flight took off:
- A late passenger "Daisy" checked in with 20kg of luggage.
- Bob’s luggage went missing.
- The staff prepared a daily report before resetting for the next flight.
"""

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

luggage2 = dict(luggage)

print(luggage2)

#print(type(luggage2))

report1 = luggage2.copy()

print(report1)

luggage2["Daisy"] = 20

print(luggage2)

luggage2.pop("Bob")

report2 = luggage2.copy()

#final_report = report1 + report2

print(final_report)
