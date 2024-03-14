import requests


def get_server_time():
    url = 'https://api.kucoin.com/api/v1/timestamp'
    response = requests.get(url)
    print(response.json())


def get_all_tickers():
    url = 'https://api.kucoin.com/api/v1/market/allTickers'
    response = requests.get(url)
    dict_tmp = response.json()
    # print(dict_tmp.keys())
    
    # tickers_list = dict_tmp['data']
    # for ticker in tickers_list:
    #     print(ticker['symbol'])
