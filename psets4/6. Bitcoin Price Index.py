import sys
import requests


if len(sys.argv) > 2:
    sys.exit("Too many arguments.")
elif len(sys.argv) < 2:
    sys.exit("Missing command-line argument.")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")

try:
    # replace YourApiKey with the actual API key as per the directions of https://cs50.harvard.edu/python/psets/4/bitcoin/
    got = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
except requests.RequestException:
    sys.exit("Try again.")

x = got.json()
data = x["data"]
usd = float(data["priceUsd"])

result = n * usd
print(f"${result:,.4f}")
