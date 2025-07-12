from sys import exit, argv
from requests import get, RequestException

if len(argv) == 1:
    exit("Missing command-line argument")

try:
    btc = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number")

while True:
    try:
        response = get("https://api.coindesk.com/v1/bpi/currentprice.json")
        break
    except RequestException:
        input("Retry")
        continue

rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
print(f"${btc * rate:,.4f}")
