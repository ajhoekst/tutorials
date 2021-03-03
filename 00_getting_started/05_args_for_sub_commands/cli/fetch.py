import click
import requests


@click.command()
@click.argument('url')
def fetch(url=None):
    response = requests.get(url)
    print(response.headers)


if __name__ == '__main__':
    fetch()
