import requests

def get_btc_price_usd():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    return data["bitcoin"]["usd"]

def usd_to_btc(usd_amount):
    btc_price = get_btc_price_usd()
    btc_amount = usd_amount / btc_price

    return btc_amount

def btc_to_usd(btc_amount):
    btc_price = get_btc_price_usd()
    usd_amount = btc_amount * btc_price

    return usd_amount


if __name__ == "__main__":
    print("Welcome to the Jabez Converter")
    print("1. USD --> BTC")
    print("2. BTC --> USD")

    choice = input("Choose conversion: ")

    if choice == "1":
        usd = float(input("Enter USD amount: "))
        btc = usd_to_btc(usd)
        print(f"${usd} = {btc:.8f} BTC")
    elif choice == "2":
        btc = float(input("Enter BTC amount: "))
        usd = btc_to_usd(btc)
        print(f"${btc} = {usd:.8f} BTC")
    else:
        print("Invalid choice.")

