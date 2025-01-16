import json
from logging import info, warning
from pathlib import Path

this_bucket = Path().cwd()

other_buckets = [
    p for p in Path("..").glob("*") if p.name != this_bucket.name and p.is_dir()
]

print(f"\n{this_bucket.name} <=> {list(map(lambda b:b.name,other_buckets))}\n")

manifests = {
    bucket: list((bucket / "bucket").glob("*.json")) for bucket in other_buckets
}


def load_manifest(app: Path):
    f = json.load(app.open(encoding="utf-8"))
    assert isinstance(f, dict)
    return f


def is_duplicate(this_app: Path):
    for bucket, apps in manifests.items():
        for app in apps:
            if this_app.stem.replace("-", "") == app.stem.replace("-", ""):
                this_ver = load_manifest(this_app)["version"]
                other_ver = load_manifest(app)["version"]
                print(
                    f"[duplicate] {this_app.stem} [{this_ver}] <=> [{other_ver}] {app.stem} in <{bucket.name}>"
                )
                return True
    return False


def should_add_checkver(app: Path):
    f = load_manifest(app)
    return not (
        "checkver" in f.keys()
        or f["url"].startswith("https://link.jscdn.cn/")
        or f["url"].startswith("https://dlink.host/1drv/")
    )


for app in (this_bucket / "bucket").glob("*.json"):
    info(app)
    is_duplicate(app)
    if should_add_checkver(app):
        warning(f"[checkver?] {app.stem}")
        warning(f"[checkver?] {app.stem}")
