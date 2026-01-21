price = 50 #cents

while price > 0:
    print(f"Amount Due: {price}")
    coin = int(input("Insert Coin: "))
    if coin in {25, 10, 5}:
        price -= coin

if price <= 0:
    print(f"Change Owed: {-price}")