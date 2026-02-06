import inflect
p = inflect.engine()

x = []

while True:
    try:
        names = input("Name: ")
        x.append(names)
    except EOFError:
        break

print(f"\nAdieu, adieu, to {p.join(x)}")