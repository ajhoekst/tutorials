import click
import requests


@click.command()
def fetch():
    response = requests.get('https://www.twitter.com')
    print(response)
