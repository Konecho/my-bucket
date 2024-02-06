import click
from search import scoop_search


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.group(context_settings={
    'help_option_names': ['-h', '--help', '/?']
})
@click.option('-v', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True, help='Show version.')
def cli():
    """This is the main command."""
    pass


@cli.command()
@click.argument('query')
def search(query):
    """Search available apps"""
    scoop_search(query)


if __name__ == '__main__':
    cli()
