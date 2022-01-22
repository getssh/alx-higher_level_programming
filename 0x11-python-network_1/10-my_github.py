#!/usr/bin/python3
'''getting user info from github using requests module'''


if __name__ == '__main__':
    import requests
    from sys import argv

    token = argv[2]
    user = argv[1]
    query_url = "https://api.github.com/users/{}".format(user)
    headers = {
              'Authorization': 'token {}'.format(token),
              'Accept': 'application/vnd.github.v3+json',
              }
    r = requests.get(query_url, headers=headers)
    data = r.json()

    print(data.get('id', 'None'))
