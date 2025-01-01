from bottle import route, run, request

@route('/currency', method='GET')
def get_currency():
    today = request.query.get('today')
    key = request.query.get('key')
    if today is not None:
        if key == 'value':
         return "USD - 41,5"

if __name__ == '__main__':
    run(host='localhost', port=8000)

    """
    Запити:
    http://localhost:8000/currency?today&key=value
    """