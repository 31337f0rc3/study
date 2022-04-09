def wsgi_application(environ, start_response):
    rs = int(environ.get('CONTENT_LENGTH', 0))    
    query = environ['QUERY_STRING'].strip()
    data = [i for i in query.split('&')]
    mstr = ''
    for el in data:
        mstr += el +'\n'
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [bytes(mstr, encoding='utf-8')]
