from mailing import Mailing

to_address = (666555, "Москва", "Барвихинская", "д.50", "77")
from_address = (777111, "Солнечногорск", "Баранова", "д. 11", "56")
track = "8736352"
cost = 1135

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
