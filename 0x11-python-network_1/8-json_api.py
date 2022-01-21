#!/usr/bin/python3
'''managing json using requests moduel'''


if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.post('http://0.0.0.0:5000/search_user')
    print(req.json())
    try:
        if len(argv) >= 2:
            q = argv[1]
            data = req.json()
            print('[{}] {}'.format(q['id'], q['name']))
        if len(argv) < 2 or req.json() == None:
            print('No result')
    except Exception:
        print('Not a valid JSON')
