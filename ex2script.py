from bottle import route, run

@route('/get', method='GET')
def get_hello():
    return "Hello World!"

if __name__ == '__main__':
    run(host='localhost', port=8000)

    """
    Запити:
    http://localhost:8000/get
    """