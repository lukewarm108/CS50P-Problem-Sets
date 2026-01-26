months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
        elif "," in date:
            date = date.replace(",", "")
            parts = date.split()
            if len(parts) != 3:
                continue
            month_str = parts[0].capitalize()
            if month_str not in months:
                continue
            m = months.index(month_str) + 1
            d = int(parts[1])
            y = int(parts[2])
        else:
            continue
        
        if m < 1 or m > 12 or d < 1 or d > 31:
            continue
        break
    except ValueError:
        continue

print(f"{y}-{m:02}-{d:02}")