import click


@click.command()
@click.argument('name')
def hello(name=None):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    hello()
