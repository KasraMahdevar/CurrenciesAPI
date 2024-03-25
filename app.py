from flask import Flask
import json
from components.getCurrencyValue import GetCurrencyValue
import datetime

app = Flask(__name__)


@app.route('/currency/<symbol>')
def currency_value(symbol: str):
    try:
        currency_object = GetCurrencyValue(currency_symbol=symbol)
    except ValueError as error:
        return f'{error}'
    else:
        currency_value = currency_object.getValue() + ' Rial'
        time = datetime.datetime.now()
        data = {
            'currency' : symbol,
            'value' : currency_value,
            'date_time': {
                'date': str(datetime.date.today()),
                'hour': str(time.hour),
                'minute': str(time.minute),
                'second': str(time.second)
            }
        }
        json_date = json.dumps(data)
        return json_date


if __name__ == '__main__':
    app.run(debug=True)
