sandwich_orders = ["1st", "pastrami", "2nd", "3rd", "pastrami", "4th", "pastrami", "pastrami", "pastrami"]
print("pastrami is sold all")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)