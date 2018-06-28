import json

import requests

base = 'https://api.iextrading.com/1.0'

def getCompanyFromIEX(company):
    route = base + '/stock/{}/company'
    try:
        req = requests.get(route.format(company))
        if req.status_code != 200:
            print(req.status_code)
        data = req.json()
        return data
    except:
        print(req.status_code)


def main():
    data = getCompanyFromIEX('aapl')
    print(json.dumps(data, indent=4))

if __name__ == '__main__':
    main()
