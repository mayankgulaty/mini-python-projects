import requests
import argparse

def get_exchange_rates(api_url):
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception("Error fetching exchange rates")
    return response.json()

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not supported")
    base_to_from_rate = rates[from_currency]
    from_to_base_rate = 1 / base_to_from_rate
    amount_in_base = amount * from_to_base_rate
    converted_amount = amount_in_base * rates[to_currency]
    return converted_amount

def main():
    parser = argparse.ArgumentParser(description='Currency Converter CLI Tool')
    parser.add_argument('amount', type=float, help='Amount to convert')
    parser.add_argument('from_currency', type=str, help='Base currency')
    parser.add_argument('to_currency', type=str, help='Target currency')

    args = parser.parse_args()

    API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
    rates = get_exchange_rates(API_URL)['rates']

    try:
        result = convert_currency(args.amount, args.from_currency.upper(), args.to_currency.upper(), rates)
        print(f"{args.amount} {args.from_currency.upper()} is equal to {result:.2f} {args.to_currency.upper()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
