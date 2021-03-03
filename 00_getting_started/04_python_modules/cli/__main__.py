import click

from .fetch_twitter import fetch
from .hello_world import hello


@click.group()
def cli():
    pass


cli.add_command(fetch)
cli.add_command(hello)
cli()
