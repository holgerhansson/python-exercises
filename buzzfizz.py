conditions = {'Fizz': 3, 'Buzz': 5, 'Zipp': 10}

for i in range (1,101):
    output = ""
    for key,val in conditions.items():
        if i % val == 0:
            output += key
    if output == "":
        print(i)
    else:
        print(output)
