import click
from hello_from import helloFrom
from hello_to import helloTo

@click.group()
def cli():
    pass

@cli.command("from", help="Say hello from someone")
@click.argument("name")
def commandFrom(name):
    click.echo(helloFrom(name))

@cli.command("to", help="Say hello to someone")
@click.argument("name")
def commandTo(name):
    click.echo(helloTo(name))

if __name__ == "__main__":
    cli()