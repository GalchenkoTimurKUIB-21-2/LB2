from bottle import route, run, request, response
import xml.etree.ElementTree as ET

@route('/data', method='GET')
def Content_Type():

    content_type = request.get_header('Content-Type')

    if content_type == 'application/json':

        response.content_type = 'application/json'
        return {"content": "content", "type": "json"}

    elif content_type == 'application/xml':

        response.content_type = 'application/xml'
        return """<?xml version="1.0"?>
        <data>
        <content>content</content>
        <type>xml</type>
        </data>"""

    else:

        response.content_type = 'application/text'
        return "without content type"

if __name__ == '__main__':
    run(host='localhost', port=8000)

    """
    Запити:
    http://localhost:8000/data
    """