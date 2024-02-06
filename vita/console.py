from typing import List
from rich.console import Console
from rich.table import Column, Table

console = Console()
terminal_width = console.width

def print_dict_list(d:List[dict]):
    table = Table(show_header=True, header_style="bold magenta")
    keys=d[0].keys()
    for dd in keys:
        table.add_column(dd)
    for dd in d:
        table.add_row(*[dd[k] for k in keys])
    console.print(table)