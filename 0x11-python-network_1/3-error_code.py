#!/usr/bin/python3
'''get request and handling http errors'''


if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.error import URLError
    from sys import argv

    try:
        with urlopen(argv[1]) as resp:
            print(resp.read())
    except URLError as e:
        print('Error code: {}'.format(e.code))
