import json

f_number = input('your favorite number')

with open("fa_number.json", 'w') as f_j:
    json.dump(f_number, f_j)