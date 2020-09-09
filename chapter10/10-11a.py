import json

with open("fa_number.json", 'r') as f_j:
    f_number = json.load(f_j)
print(f_number)