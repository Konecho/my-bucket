# my-bucket
添加
```ps
scoop bucket add my-bucket https://github.com/Konecho/my-bucket
```
模板
```json
{
    "homepage": "主页",
    "description": "介绍",
    "license": "",
    "version": "版本号",
    "url": "下载链接（.exe#/dl.7z）",
    "hash":"算法:值",
    "extract_dir": "如果文件在一个子文件夹内，展开的文件夹名",
    "pre_install": [
        "if (!(Test-Path \"$persist_dir\\配置文件.ini\")) { New-Item \"$dir\\配置文件.ini\" | Out-Null }"
    ],
    "bin": "可执行文件",
    "shortcuts": [
        [
            "某个执行程序.exe",
            "快捷方式的名称"
        ],
        [
            "bin\\子目录程序.exe",
            "快捷方式"
        ]
    ],
    "persist": [
        "文件夹",
        "文件夹2",
        "配置文件.ini"
    ],
    "checkver":{
        "url": "检查链接",
        "regex": "点击下载 程序名([\\d.]+)程序后缀"
    },
    "autoupdate": {
        "url": "下载链接$version（.exe#/dl.7z）",
        "extract_dir": "程序名$version"
    },
    "notes": "附注"
    
}
```
可选替代
```json
{
    "_comment":"",
    "pre_install":[
        "function CreateFile([String] $file, [String] $content = $null) {",
        "    if (!(Test-Path \"$persist_dir\\$file\")) {",
        "        New-Item -Force -Path \"$persist_dir\\$file\" -ItemType file -Value $content | Out-Null",
        "    }",
        "}",
        "CreateFile 'path/config.ini'",
    ],
    "architecture": {
        "64bit": {
            "url": "url64",
            "hash": "hash64",
            "extract_dir": "dir64",
            "bin": [
                [
                    "bin64.exe",
                    "bin"
                ]
            ]
        },
        "32bit": {
            "url": "url32",
            "hash": "hash32",
            "extract_dir": "dir32",
            "bin": [
                [
                    "bin32.exe",
                    "bin"
                ]
            ]
        }
    },
    "bin": [
        "program.exe",
        [
            "program.exe",
            "alias",
            "--arguments"
        ]
    ]
    
    
}
```
