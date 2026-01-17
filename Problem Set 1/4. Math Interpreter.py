x, y, z = input("Expression: ").split(" ")
x = int(x)
z = int(z)

if y == "+":
    z = x + z
elif y == "-":
    z = x - z
elif y == "*":
    z = x * z
else:
    z = x / z

print(float(f"{z:.1f}"))