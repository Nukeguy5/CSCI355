
import click
import sfs

@click.command()
def help():
    click.echo("\nCommands are:")
    click.echo("\tformat")
    click.echo("\tmount")
    click.echo("\tdebug")
    click.echo("\tcreate")
    click.echo("")

@click.command()
def format():
    sfs.fs_format()


@click.command()
def mount():
    sfs.fs_format()

@click.command()
def debug():
    sfs.fs_debug()

@click.command()
def create():
    sfs.fs_create()
