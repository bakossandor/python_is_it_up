import click
from main import isup

@click.command()
@click.argument("website")
def cli(website):
    """A simple cli program which check if a web-site is up\n
    It accepts 1 arguments - the website domain name \n
    example: >isup "google.com"
    """
    click.echo(isup(website))
