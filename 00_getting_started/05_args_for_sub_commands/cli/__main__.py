import click

from .hello import hello
from .fetch import fetch


@click.group()
def cli():
    pass


cli.add_command(fetch)
cli.add_command(hello)
cli()
