#!/usr/bin/python3
'''fetching information from server
'''


if __name__ == '__main__':
    from urllib.request import urlopen

    with urlopen('https://intranet.hbtn.io/status') as resp:
        data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
