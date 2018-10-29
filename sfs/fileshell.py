
import click
import diskpy
import sfs

@click.command()
def help():
    print("Commands are:")
    print("\tformat")
    print("\tmount")
    print("\tdebug")
    print("\tcreate")