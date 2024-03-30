HELP='''
交互式scoop配方创建
指令：
创建，询问必须的属性：app名，版本号，安装包下载url；
开始调用scoop下载，得到hash，解包看到目录结构；
添加一个app快捷方式；
添加一个bin快捷方式；
写入文件；
读取文件；
添加一个persist目录；
生成一个文本persist；
生成electron风格的安装脚本；
'''
import json
from pathlib import Path
import re
import subprocess
# cache_path = Path(subprocess.run('scoop config cache_path',
#                   shell=True, capture_output=True, text=True).stdout)

manifest = None

def create_new():
    global manifest
    app_name = input('input app name:\n')
    if len(app_name) == 0:
        app_name = 'test'
    
    res = ''
    while len(res) == 0:
        res = input(f'please input version:\n')
    version=res

    res = ''
    while len(res) == 0:
        res = input(f'please input download url:\n')
    url=res

    if manifest is not None:
        print(manifest)# 以防不小心覆盖
    manifest={
        'version':version,
        'url':url,
    }



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



json_file = f'{app_name}.json'

json.dump(manifest, Path(json_file).open('w'))

dlinfo = subprocess.run(['scoop', 'download',
                         f'{Path(json_file).absolute()}'], shell=True, capture_output=True, text=True)

dlhash = re.search('[0-9a-f]{64}', dlinfo.stdout)[0]
if len(dlhash) == 64:
    print(dlhash)
    manifest['hash']=dlhash
else:
    ask_option("hash")
ask_option('homepage')
ask_option("description")
ask_option('license')

ask_option("extract_dir")
ask_list("persist")
create_null("shortcuts", [["app.exe", "app"]])

check_ver = ask_option("checkver")
if check_ver == 'github':
    cv = {}
    if not '🐱' in manifest['homepage'].replace('github', '🐱'):
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
with open(app_name+'.json', 'w+', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
