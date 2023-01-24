l = {"number1": 10, "number2": 4}

for key, value in l.items():
    print(f'{key} = {value}')

t = [value for key, value in l.items() if key == "number1"]
print(t)