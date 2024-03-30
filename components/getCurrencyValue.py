import requests
from bs4 import BeautifulSoup
import configparser


class GetCurrencyValue:

    def __init__(self, currency_symbol: str):
        self.__url = 'https://www.tgju.org/currency'
        config = configparser.ConfigParser()
        config.read("./static/config_files/currency_names.ini", encoding='utf-8')
        if currency_symbol in config['Names']:
            self.__currency_name = config['Names'][currency_symbol]
        else:
            raise ValueError('Waehrung (Symbol) nicht in der Liste vorhanden.')


    def getValue(self):
        try:
            response = requests.get(self.__url)
        except requests.exceptions.HTTPError as error:
            print(f'HTTP-Fehler: {error}')
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            tds = soup.find_all('td')
            for td in tds:
                th_tags = td.find_previous_sibling('th')
                if th_tags and th_tags.text.strip() == self.__currency_name:
                    return td.text



