from wsgiref.simple_server import make_server
from urllib.parse import parse_qsl
import json

names = {
    'Cyberman': 'John Lumic',
    'Dalek': 'Davros',
    'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
    'Human': 'Leonardo da Vinci',
    'Ood': 'Klineman Halpen',
    'Silence': 'Tasha Lem',
    'Slitheen': 'Coca-Cola salesman',
    'Sontaran': 'General Staal',
    'Time Lord': 'Rassilon',
    'Weeping Angel': 'The Division Representative',
    'Zygon': 'Broton'
}

def application(environ, start_response):

    parsed_url_query = parse_qsl(environ['QUERY_STRING'], keep_blank_values=True)
    if environ['QUERY_STRING'] and parsed_url_query[0][-1] in names:
        name = parsed_url_query[0][-1]
        status = '200 OK'
        response_body = json.dumps({"credentials": names[name]}).encode('utf-8')
    else:
        status = '404 Unknown'
        response_body = json.dumps({"credentials": "unknown"}).encode('utf-8')

    response_headers = [
        ('Content-Type', 'application/json')
    ]

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 8888, application)
httpd.serve_forever()
