import json

manifest = {}
app_name = input('input app name:\n')
if len(app_name) == 0:
    app_name = 'defalut'


def ask_required(name):
    global manifest
    res = ''
    while len(res) == 0:
        res = input(f'please input [{name}]:\n')
    print(res)
    manifest[name] = res
    return res


def ask_option(name):
    global manifest
    res = input(f'please input [{name}]:\n')
    if len(res) == 0:
        print('skipped')
        return
    print(res)
    manifest[name] = res
    return res


def ask_list(name):
    global manifest
    res = []
    while True:
        i = input(f'please input [{name}]:\n')
        if len(i) == 0:
            break
        res.append(i)
        print(res)
    if len(res) > 0:
        manifest[name] = res
    else:
        print('skipped')


def ask_pre_inst():
    pass


def create_null(name, value):
    global manifest
    manifest[name] = value


ask_required('homepage')
ask_required("description")
ask_option('license')
ask_required("version")

ask_required("url")
ask_option("hash")
ask_option("extract_dir")
ask_list("persist")
create_null("shortcuts",[["app.exe","app"]])

check_ver = ask_option("checkver")
if check_ver == 'github':
    cv = {}
    if not '🐱' in manifest['homepage'].replace('github','🐱'):
        cv['github'] = input('please input github url:\n')

    while True:
        new_url = manifest["url"].replace(manifest["version"], "$version")
        res = input(f'use autoupdate url: {new_url} \n yes/no?\n')
        if str(res).startswith('y'):
            cv['url'] = new_url
            break
        elif str(res).startswith('n'):
            print('please fix it yourself')
            cv['url'] = new_url
            break
    manifest["autoupdate"] = cv
ask_option("notes")
print(manifest)
with open(app_name+'.json', 'w+',encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
