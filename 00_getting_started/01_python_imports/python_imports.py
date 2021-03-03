import requests


if __name__ == '__main__':
    response = requests.get('https://www.twitter.com')
    print(response)
