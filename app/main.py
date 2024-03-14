import os
import json

from dotenv import load_dotenv

from kucoin_api import get_server_time, get_all_tickers


load_dotenv()


def main():
    get_server_time()
    get_all_tickers()
    current_dir = os.getcwd()
    
    file_path = os.path.join(current_dir, 'settings.json')
    with open(file_path) as file:
        data = json.load(file)
    
    print(data)
    # json.load()
    print(os.getenv('KUCOIN_TOKEN'))

if __name__ == '__main__':
    main()