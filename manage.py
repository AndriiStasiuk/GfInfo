"""This module contains needed methods for correct service starting."""

import click

from gw_info_api.app import app
from gw_info_api.utils.logger import log


@click.group()
def command_group():
    """Init command group."""
    ...


@command_group.command()
@click.option("--host", default='127.0.0.1')
@click.option("--port", default=5001)
@click.option("--workers", default=1, type=int)
def runserver(host: str, port: str, workers: int):
    """Setup params and run server.

    Args:
        host (str): Host where server will be running.
        port (str): Port where server will be running.
        workers (int): Count of workers.

    """

    app.run(host=host, port=port, workers=workers)


if __name__ == "__main__":
    try:
        command_group()
    except Exception as error:
        log.critical(f"Error occurred: {error}")
        exit(1)
