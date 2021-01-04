import requests

session = '53616c7465645f5f971047d77726f968dd2a83ffbb8adee5d4399ea322afa67e063763ad79a1caabaf22b3d5fe039b04'
cookies = dict(session=session)

def get(day: int):
    url = 'https://adventofcode.com/2020/day/' + str(day) + '/input'
    r = requests.get(url, cookies=cookies)

    return r.content.decode()
