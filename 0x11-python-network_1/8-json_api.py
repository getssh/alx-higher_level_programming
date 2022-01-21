#!/usr/bin/python3
'''managing json using requests moduel'''


if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) >= 2:
        data = {'q': argv[1]}
    else:
        data = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        j_data = req.json()
        if j_data['id'] is None:
            print('No result')
        else:
            print('[{}] {}'.format(j_data['id'], j_data['name']))
    except Exception:
        print('Not a valid JSON')
