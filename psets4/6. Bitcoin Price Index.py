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
    got = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=b1b533f37a14fec3cb0e2f6137f56abf5c3a3f8b4b73600833fdcbd9caa76bb2")
except requests.RequestException:
    sys.exit("Try again.")

x = got.json()
data = x["data"]
usd = float(data["priceUsd"])

result = n * usd
print(f"${result:,.4f}")