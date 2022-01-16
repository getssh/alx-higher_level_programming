#!/bin/python3
'''requesting a post request to server with values(variable&value)
'''


if __name__ == '__main__':
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import urllib
    from sys import argv

    url = argv[1]
    with urlopen(url) as resp:
        print(resp.info()['X-Request-Id'])
