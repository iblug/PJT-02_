import requests

def get_btc_krw():
    BASE_URL = 'https://api.bithumb.com/public/ticker/'
    order_currency = 'BTC'
    payment_currency = 'KRW'

    res = requests.get(BASE_URL+order_currency+'_'+payment_currency).json()
    data = res.get('data')
    prev_closing_price = data.get('prev_closing_price')

    return prev_closing_price

if __name__ == "__main__":
    print(get_btc_krw())