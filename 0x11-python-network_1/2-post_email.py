#!/usr/bin/python3
'''sending a post request with email variable'''


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    import urllib
    from urllib.parse import urlencode
    from sys import argv

    email_value = {'email': argv[2]}
    data = urlencode(email_value)
    data = data.encode('UTF-8')
    req = Request(argv[1], data)
    with urlopen(req) as resp:
        print(resp.read().decode('UTF-8'))
