ciudades = ["mveracruz", "mexico", "oaxaca", "xalapa,", "monterrey"]
i = ciudades[0][0]
print(i)
for ciudad in ciudades:
    if ciudad[0] == "m":
        print(f' la ciudad {ciudad} empienza con la leta m')
    else:
        print(f'la ciudad {ciudad} no empienza con la leta m')