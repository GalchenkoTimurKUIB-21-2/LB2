from bottle import route, run, request, response
from datetime import datetime, timedelta
import requests

NBU_API_URL = "https://bank.gov.ua/NBU_Exchange/exchange_site"

def get_usd_exchange_rate(date: str):

    params = {
        "valcode": "USD",
        "date": date,
        "json": ""
    }
    response = requests.get(NBU_API_URL, params=params)
    data = response.json()
    return data[0]["rate"]

@route('/currency', method='GET')
def get_currency():

    today = request.query.get('today')
    yesterday = request.query.get('yesterday')

    day = datetime.now()

    if today is not None:
        date = day.strftime("%Y%m%d")

    elif yesterday is not None:
        date = day - timedelta(days=1)
        date = date.strftime("%Y%m%d")

    rate = get_usd_exchange_rate(date)

    return {"date": date, "rate": rate}

if __name__ == "__main__":
    run(host="localhost", port=8000)

    """
    Запити:
    http://localhost:8000/currency?today
    http://localhost:8000/currency?yesterday
    """