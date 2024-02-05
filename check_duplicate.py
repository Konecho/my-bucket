from pathlib import Path
import json

this_bucket_name = Path().cwd().name

other_bucket_list = [p for p in Path('..').glob(
    '*') if p.name != this_bucket_name]
print(f"\n{this_bucket_name} <=> {other_bucket_list}\n")


def is_duplicate(app: Path):
    for bucket in other_bucket_list:
        if (bucket/'bucket'/app.name).exists():
            this_ver = json.load(app.open(encoding='utf-8'))['version']
            other_ver = json.load(
                (bucket/'bucket'/app.name).open(encoding='utf-8'))['version']
            print(
                f'[duplicate] {app.stem} [{this_ver}] <=> [{other_ver}] in <{bucket.name}>')
            return True
    return False


def should_add_checkver(app: Path):
    f = json.load(app.open(encoding='utf-8'))
    assert isinstance(f, dict)
    return not ('checkver' in f.keys()) and (not (f['url'].startswith('https://link.jscdn.cn/' or f['url'].startswith('https://dlink.host/1drv/'))))


for app in Path('./bucket').glob('*.json'):
    is_duplicate(app)
    if should_add_checkver(app):
        print(f'[checkver?] {app.stem}')
