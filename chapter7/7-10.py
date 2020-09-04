responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    place = input("if you could visit one place in the world,where would u go?")
    responses[name] = place

    repat = input("would u again? y or n?")

    if repat == "n":
        polling_active = False

print("-----Poll result-----")
for name, place in responses.items():
    print(f"{name}'s place is {place}'")