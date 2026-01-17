def main():
    x = input("What time is it? ")
    x = convert(x)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")

def convert(time):
    if " " in time:
        t, p = time.split(" ")
        h, m = t.split(":")
        h = float(h)
        m = float(m)
        if p == "a.m.":
            if h == 12:
                h = 0
        elif p == "p.m.":
            if h != 12:
                h = h + 12
    else:
        h, m = time.split(":")
        h = float(h)
        m = float(m)
    m = m / 60
    return h + m
    

if __name__ == "__main__":
    main()