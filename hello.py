

def app(env, start_response):
    from io import StringIO
    stdout = StringIO()
    answers = env['QUERY_STRING'].split('&')
    for answer in answers:
        print(answer, file=stdout)
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, headers)
    return [stdout.getvalue().encode('utf-8')]