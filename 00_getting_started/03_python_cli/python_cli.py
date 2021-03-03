import click

import fetch_twitter
import hello_world


@click.group()
def cli():
    pass


cli.add_command(fetch_twitter.fetch)
cli.add_command(hello_world.hello)


if __name__ == '__main__':
    cli()
