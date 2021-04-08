from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def load_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '500',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '7f5a40b9-623d-4ff2-84c6-b5033dc8e924',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        with open("latestprices.json", "w") as zfile:
            json.dump(data, zfile)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def main():
    load_data()

if __name__ == '__main__':
    main()