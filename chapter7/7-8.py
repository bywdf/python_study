sandwich_orders = ["1st", "2nd", "3rd", "4th"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"i made your{order}")
    finished_sandwiches.append(order)
print( sandwich_orders)
print(finished_sandwiches)