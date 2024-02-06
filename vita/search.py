import click
from pathlib import Path
import re
from console import print_dict_list

import json


def colored(text:str):
    text=text.replace('\\','/')
    return text
    return f"[bold cyan]{text}[/bold cyan]"


def highlight_match_text(text, pattern):
    matches = list(re.finditer(pattern, text))
    if (len(matches)):
        start, end = matches[0].span()
        return text[:start] + colored(text[start:end]) + text[end:]
    return text


def color_matched(bins: list, query: re.Pattern):
    if bins is None:
        return []
    bins = bin_to_list(bins)
    return [highlight_match_text(b, query) for b in bins]


def bin_to_list(bin):
    if isinstance(bin, str):
        return [bin]
    return [b[0] if isinstance(b, list) else b for b in bin]


def bin_match(manifest: dict, query: re.Pattern):
    if not 'bin' in manifest.keys():
        return False
    bins = bin_to_list(manifest['bin'])
    if len([b for b in bins if len(query.findall(b))]):
        return True
    return False


def app_info(app: Path, query: re.Pattern):
    info = json.load(app.open(encoding='utf-8'))
    return {'name': app.stem,
            'version': info['version'],
            'bin': '|'.join(color_matched(info.get('bin'), query))
            }


def search_bucket(bucket: Path, query: re.Pattern):
    apps = (bucket/'bucket').glob('*.json')
    return [{**app_info(app, query),
             'bucket': (bucket).resolve().stem,
             } for app in apps if len(query.findall(app.stem)) or bin_match(
        json.load(app.open(encoding='utf-8')), query)]


def get_local_bucket():
    return list(filter(lambda p: (p/'bucket').exists(), (Path('D:\Scoop')/'buckets').glob('*')))


def scoop_search(query_str):
    try:
        query = re.compile(query_str)
    except Exception as e:
        click.echo(f'Invalid regular expression: {query_str}\n')
        raise e
    res = []
    for bucket in get_local_bucket():
        res.extend(search_bucket(bucket, query))

    if not (len(res)):
        click.echo(f"WARN  No matches found. `{query}`")
    else:
        click.echo(f"Results from local buckets... `{query}`")
        print_dict_list(res)


if __name__ == '__main__':
    print(bin_match(json.load(Path('./bucket/activetcl.json').open()), re.compile('tcl')))
    scoop_search('rt')
