#!/usr/bin/python3
'''request id from headers'''


if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get(argv[1])
    resp = req.headers['X-Request-Id']
    print(resp)
