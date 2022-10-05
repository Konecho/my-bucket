from pathlib import Path
import json
Path()
this_bucket_name=Path().cwd().name
print(this_bucket_name)
other_bucket_list=[p for p in Path('..').glob('*') if p.name!=this_bucket_name]
print(other_bucket_list)
for app in Path('./bucket').glob('*.json'):
    for bucket in other_bucket_list:
        if (bucket/'bucket'/app.name).exists():
            this_ver=json.load(app.open(encoding='utf-8'))['version']
            other_ver=json.load((bucket/'bucket'/app.name).open(encoding='utf-8'))['version']
            print(f'duplicate app {app.stem}[{this_ver}] <=> bucket {bucket.name}[{other_ver}]')


