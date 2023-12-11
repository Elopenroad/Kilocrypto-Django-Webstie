from pycoingecko import CoinGeckoAPI
import time
import json

def coin():
    cg = CoinGeckoAPI()

    prices = cg.get_search_trending()
    coins = prices['coins']

    coinList = []

    for item in coinList:
        data_json = json.dumps(item) 
        print(data_json)
        data_dict = json.loads(data_json)
        name = data_dict['Name']
        changes = data_dict['24h_Change']
        print(f"{name} and changes {changes}")

    return name , changes

