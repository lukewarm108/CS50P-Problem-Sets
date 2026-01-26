lst = {}

while True:
    try:
        items = input().lower().strip()
        if not items in lst:
            lst[items] = 1
        else:
            lst[items] += 1
    except EOFError:
        break

print()
for item in sorted(lst):
    result = (f"{lst[item]} {item}").upper()
    print(result)