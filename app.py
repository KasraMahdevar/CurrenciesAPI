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
        status = 404
        data = {
            'status': status,
            'body': {
                'error_text': str(error)
            }
        }
        json_format = json.dumps(data)
        return json_format
    else:
        currency_value = currency_object.getValue() + ' Rial'
        status = 200
        time = datetime.datetime.now()
        data = {
            'status': status,
            'body': {
                'currency': symbol,
                'value': currency_value,
                'date_time': {
                    'date': str(datetime.date.today()),
                    'hour': str(time.hour),
                    'minute': str(time.minute),
                    'second': str(time.second)
                }
            }

        }
        json_format = json.dumps(data)
        return json_format


if __name__ == '__main__':
    app.run(debug=True)
