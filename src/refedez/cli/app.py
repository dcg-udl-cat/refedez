import typer

from refedez.cli.commands.start import start as start_impl
from refedez.cli.commands.status import status as status_impl
from refedez.cli.commands.stop import stop as stop_impl
from refedez.cli.commands.clean import clean as clean_impl

app = typer.Typer()

DEFAULT_CONFIG_FILE = "./refedez.yaml"
DEFAULT_PATH_FLAG = typer.Option(DEFAULT_CONFIG_FILE, help="Path to the config file")


@app.command()
def start(path: str = DEFAULT_PATH_FLAG):
    start_impl(path=path)


@app.command()
def status(path: str = DEFAULT_PATH_FLAG):
    status_impl(path=path)


@app.command()
def stop(path: str = DEFAULT_PATH_FLAG):
    stop_impl(path=path)


@app.command()
def clean(path: str = DEFAULT_PATH_FLAG):
    clean_impl(path=path)
