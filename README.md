# my-bucket
添加
```ps
scoop bucket add my-bucket https://github.com/Konecho/my-bucket
```
[快速生成json](https://json-editor.github.io/json-editor/?data=N4Ig9gDgLglmB2BnEAuUMDGCA2MBGqIAZglAIYDuApomALZUCsIANOHgFZUZQD62ZAJ5gArlELwwAJzplsrEIgwALKrNSgAJEtXqUIZVCgQUAelMda8ALQ61ZAHTSA5qYAmUskSjWADABZTO1kAYgUoQQgqQjBObnE2CClIKilYGg0DeioIMmdotBAIqMJEKCkYeGcFNxoMCug4eEJAe3jAN7lAbjlAVwyFEhkycX0RCpAAXzZapQbYBEzigsVyyuqJuummwkB540AH+LG2XAwqJALQedKlqpq1mEbZ/UAI40Bhc0B5ZUA66L2QADdUxA3Cs/0ZQql1WUxuM2a+kAEk6AGnNAO/KClyRlSkJAAG1fNYAJwOAC6AGoPsN5P9IgsgcsrmDbqjANBygF94wB/KYBS4w+yjIiGUczJ52BKxAk3q4L+IEAhBaAGKzAIAeHyoAA9ymQeLw3DApNySoCLvzBes7iBAAvGgDXlQB3boBVfQ+eEq6vJWqpQpphEA98qAcyNADIRgHDTNofTnSKAYMTIUkakBkKSeQQKGBQNSB048/Sh8OR6N0WNFeOLPkfHXCvVyqiAGJVANf6gHdjQCdpoB4fQUdEqAEkU4GAExsWSy+sx1CN8YC64O/SlysfJJUXiVMpyElx4OJoTJjtBm1Z7s5vsgQAhGW7AL4qgBO5Ic/GBla2EGcRthR+dTxeU5e9iGEQAvfoBAY09HxU3AA1t81QuYnEeIjkiiNIYAyQpiSPTUlzYKQqHyWUIMza8b2pO9oRhQABi0AU/MFBggBHERVSoNxUDRXFuzIMRRAgNwBhOdNg1iLh/0SQDUnSNNwJ/SDKVBe1UJABkWTZDkuS4xCQR7FCRQlGV5U8JUVW/S9eR4yS+JFI0zTGZD1L1QArwMACqVABezQAG0w+SRozTAFxO1W8RUAC5tAHhDQBouUATwztOgqh8MI4iUDRLIGFyfIFC/X5ZjYcC2EtZoyLYH0KF4VJkikQMQEqaN5LvNgoF0BY8DAMAoCBMgIH8HCvIImC3F4PBBGVKgiAo7BBka7BECoCYDwgAQ6rwyqiN4HAIxQVr2ri5QwASyA+CtFByhEDqQEkXgyDcFUITkXgkhSYDQNGxayA4Mh4JGuQxoFA8yDwbARyIqNeEsO59s6xArpu3gsGwAQIHa1Bnou17rpHbagPYv6zsWlVAfek8VrW8G2shy6gZWsMhF4GDpFqb9/qht6R1h2obujBHzqOfHUfDD7IGG/7YaweByjANreCgSBSaR6GCbRuqiaoaMVq+jHJsDXHkZhnn6uJkcBDKYWKA50ZRiAA===)

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
