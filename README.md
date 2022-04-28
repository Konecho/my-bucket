# my-bucket
更新方法：在根目录执行 `.\bin\checkver.ps1 -u`

添加
```ps
scoop bucket add my-bucket https://github.com/Konecho/my-bucket
```
[JSON Schema(ver1)](https://json-editor.github.io/json-editor/?data=N4Ig9gDgLglmB2BnEAuUMDGCA2MBGqIAZglAIYDuApomALZUCsIANOHgFZUZQD62ZAJ5gArlELwwAJzplsrEIgwALKrNSgAJEtXqUIZVCgQUAelMda8ALQ61ZAHTSA5qYAmUskSjWADABZTO1kAYgUoQQgqQjBObnE2CClIKilYGg0DeioIMmdotBAIqMJEKCkYeGcFNxoMCug4eEJAe3jAN7lAbjlAVwyFEhkycX0RCpAAXzZapQbYBEzigsVyyuqJuummwkB540AH+LG2XAwqJALQedKlqpq1mEbZ/T2QADdUxA3Cs/0yisvVqZuZ5r6QASToAac0A78oKXJGVKAkAAbV81gAnA4ALoAagew3k70iCy+yyuf1usMA0HKAX3jAH8pgFLjB7KMiIZRzPHnb4rECTer/N4gQCEFoAYrMAgB4PKgAD3KZB4vDcMCkzJKnwu7M56zuIEAC8aANeVAHdugFV9B54Sry/FKolckmEQD3yoBzI0AMhGAcNM2g9GdIoBgxMhcQqQGQpJ5BAoYFA1J7Tiz9L7/YHg3RQ0Vw4s2Q8Vdy1WKqIAYlUA1/qAd2NAJ2mgHh9BR0SoASRjnoATGxZKLyyHUJXxhzrhb9LnCw8klReJUynIcWHvZGhNGG16TUnfuaAYRk63Z/pACEZdsAviqAE7kuy8YGVjYQRwG2EHx0PJ4Tmym2yBAC9+gEBjR0PFTcADWzzlE9ZhOnqthgADvQDIZoAEP8AOTOEGygiHgwGAGhGgCqyoAFhGAH3xBaAJD/DxkGIogQG4AwnPG3qxFwPCQskURpDAGSFNie6KlOLbEouIAUjSdIMkyH60V+9EzjyAoiuKnhSjK76np+PzcT+hBanqYwXguPKAFeBgAVSoAL2aAA2mDySMGcYfImXGXoxgAXNoA8IaANFygCeGbJbBSFQACOIiylQbioHCWQMLk+QKG+ryzGw1Got+qawiZgBY/4AZN5goAvwmAFjygDVEcpgA28YAknLOsoYAULwqTJFInogJUwaCbObBQLoCx4GAYBQF8ZAQP4Cg2fZjluLweCCNKVBEBh2CDJ12CIFQEw7hAAhtQ1Dk2c1OABigvX9WwLoZZAfBGig5QiANICSLwZBuDKAJyLwSQpORlGzRtZAcGQoqoGdg2IGQeDYD2TlBrwlh3LdHI7g9T28Fg2ACBA/U3XIc1ffdj09kdZHpJ6n0yhDv0Httu0g31G0Iz9PbIzZ0i1O+8PfZD21+kI7VPcGaNg0cWMk/6f2QNNn3I1g8DlGAfW8FAkBUxjRNI6TbW1BT2MA7wyQUHDoN84j2OC+TVDBvwDJ8BLvOjKMQA==)

[JSON Schema(ver2)](https://json-editor.github.io/json-editor/?data=N4Ig9gDgLglmB2BnEAuUMDGCA2MBGqIAZglAIYDuApomALZUCsIANOHgFZUZQD62ZAJ5gArlELwwAJzplsrEIgwALKrNSgAJEtXqUIZVCgQUAelMda8ALQ61ZAHTSA5qYAmUskSjWADABZTO1kAYgUoQQgqQjBObnE2CClIKilYGg0DeioIMmdotBAIqMJEKCkYeGcFNxoMCug4eEJAe3jAN7lAbjlAVwyFEhkycX0RCpAAXzZapQbYBEzigsVyyuqJuummwkB540AH+LG2XAwqJALQedKlqpq1mEbZ/T2QADdUxA3Cs/0yisvVqZuZ5r6QASToAac0A78oKXJGVKAkAAbV81gAnA4ALoAagew3k70iCy+yyuf1usMA0HKAX3jAH8pgFLjB7KMiIZRzPHnb4rECTer/N4gQCEFoAYrMAgB4PKgAD3KZB4vDcMCkzJKnwu7M56zuIEAC8aANeVAHdugFV9B54SryhZkKSeQQKGBQNTIXEKkCm82W610W2nFmKtkPOiVACSLttACY2LJRf6bahA+MOdcSYRAPfKgHMjQAyEYBw0zaD0Z0igGDEbqKHodZqEzojdpNxYtbCtZfd9oJl2jKu5arFVEAMSqAa/1AO7GgE7TQDw+goffBw67IyGyGGA5Gm7GAYQewOHkkqLxKmU5Di6xWndXp+XWYTfly4/dZ8T5/pACEZKcAviqAE7lly8YGVjYRHSW97WC/WlQ9m6eICAC9+gCAxumDwqNwADWzxyge+ixFwPCQskURpDAGSFNib6eoS0ZSFQ+SijhixetGzhWsoIgEPBpF4eeJ6XiAgBXgYAWdqAJJyCgEQAjiIspUG4qBwqi0ZkGIogQG4AwnD+CyIfEKEpOhmGgNhtENsqc48hSNJ0gyTLqX+x6qrCAoiuKnhSjKcHboePwxhePJanqYwMSZhDMYAFUqAC9mgANpg8kjWvmHx0fZAFMYAFzaAPCGgDRcoAnhmuWwPF8QRgkoHCWQMLk+QKLBryzGw2GosZLawtFgBY/4AZN5goAvwmAFjygDVEV5gA28Zx0ZZhQvCpMkUi2iAlTWpZ85sFAugLHgYBgFAXxkBA/hcVQvH8W4vB4II0pUEQYnYIMW3YIgVATC+EACOtyXLbwOAWige0HWwHWXdAa6AuUIiHSAki8GQbgygCci8EkSnpLat3vWQHCTqgoNHYgZB4Ngq4CVavCWHc0Mci+cMI7wWDYAIEAHVDch3RjsPw6ugNocDRP7e9Mpk9jH7rd9aXo/TWOrkzvAEdItRwWzmPk19lYbQj1o0yTRwc8L5o45A13o1zWDwOUYD7bwUCQBLdOC4zIu1GLnN49zYAUCDxM6wznP61Qhv8AyfDJBQ2ujKMQA=)

[JSON Schema(官方)](https://json-editor.github.io/json-editor/?data=N4Ig9gDgLglmB2BnEAuUMDGCA2MBGqIAZglAIYDuApomALZUCsIANOHgFZUZQD62ZAJ5gArlELwwAJzplsrEIgwALKrNSgAJDAAmhZVCgQUAehNKwkAHSJlJnVLJEo5lWrIBiBZqWr1KEAMjUxMOWngAWl93K2kAc3tHZwiABgB2Vz9PBTIdHRhYBDkABSlIKilYGlQiOUQqNh0qIhh4ArgkDUCyW2KyQwr4Loh+qEHCAD0ACgBtMgiiAEEIgDEUiIBOAF1gADYAFgBfAB8p2zIARmPzgCZGXevlMkYLm+O6HUYAShRZ+aXVuttsAAMw3E5zBbLNabHb7FIQ/7QoE7A6IqGA2HAV4ADkOXy+mgUUEEECohEQUCkrTiIEObCeti6ZHgggA8kRUDMtFJmoQPPZmq12ghECZGco+gMpEN6egxnRkGgQJpeZyAgKmi02oUkOKepLRuN6SA6K0AJIKpUXNgksmEMhSRyCBQiNoARxEVEtaiVVK9hy2JolAFEAB5Usg8DrMvIi+AlMpkyowaooWrYepsCBJipVJWgbV6ZUkGT9Qi8uJUMPE0nkgKU6nwWmNGgYanQGMBADKZAYAAIev2AOSV6vDulsMc1kvSWTiALT2v2htUmmTkAcCDDI0yyYAHX3mhmVhmWysACoiba6xS182FE0lB3dYRewOh8OwggRlBlBOTW/eBf2UHdpSGAIJkPY9T3PK9l3rRR71pE0wxAro7UQxt1xNOgwCaLoqHgEQ6C5EAdDACh4GwMBcgUatIx4BQgIUND+lAqcdE5NgGHIXB4AAawUEhEFsEQCDYWgRCkDBmnickgxvFdQCIkiyI+ZhJKeC4FFue5dKeF4bhALZW2fGBOwQQgABEqBzbh+ioHQWH7CV+0w/sYEQfsmjGGRWicwcxHofpMDkbAXRNaT5GVFl2XVbliDncsAmkmAELvJsUJYUBfz8iCQGmaDouOaC8B6Khoq+U9DwoQ8dC2ABqa8QEwzKcJykA8vGSDLymYqpGwUqj3K+oqsvFq2tXLK6SDE0pvYLgmJNR0VAKbgoGk+tQFyfJdUTcoUzTDMsy63MjoLEA8FaLpVT5DVBW1eMxWw5s2SkRYnSEDlu2QxB3sWeBPudDlge+ohfqy5ATTcDABIANwqW61X5R7hV1MVYYRpGTSI+HeF23h0OVO71RATUhR1DoXuQgGvviyGaWhtg8d4eoF1ABawE4DaNwYxweF4fIpGR+7ybRqnRXMWmPvpn6/o3CVRbJimnox/UmRNVpKXCpGSZRh6tXR6mTG1vjsBxnjEHS/WxdV42pdeuI6ZBiGFbM9sLNfAJbPsjBHL0E0IDASleDN8LldRo3Jb1J2XfBxnm2Zs6qDDpBzcjw3Kee6WsvjhmFZNWxpCgDAxEu0mo+z9Xi8qMuoEQMHIrYN1w+wC2RdtlWJZz1v091kWosGzPxej3vqXzjkAFVqWh+bbwCbmlvEFa5aWNfE7iS71sVLod8uhanY3M14B9XeUBtVqF5AR1nWPi0rVQS+FtvoQN1r0vy6bvfH+VfeMOvkfXCD9fSoBuDxMgYYz5Kn2EpRCr9m6mhAefZ+18EEbjIMFEQEAdCOVjHtDoB1kz5hqHUBoZ1DokNijJZQ60eBbXwfGIheZUxKhOuQnMlDWFdDBNdDmN84z7WwKULhx0yHZnOlQlSEYBZ8GFgAlcSEZpDxioWZKC4QBpQytNDq3QmRdyrmrE2oYZFRlfIceeiil68xNAcPhjChEiOIdw9M4iKHOLTNIxiciYCd05oA5CG5opdFLPOQgWi4HtQfMGA0I97YxzFCY7xMYLGRMXjzZaljELWOWizUxgt5HKkPoEmJ+ieR2x7urJJsiUlsEkGMOJlSTZx1lq7TeydgmzjLBoiJV9FFAKyYQHJK82BY0Rn4m+rIORcjUd0isVAqw1jSUojqO1BGEOEZIlx7CJGiMunEAoyhxIhPUeE6k2iVnRKnNtJKczFwLOrBco+HsXxdhAO+Kgg5vKjgeWGAC1zFknLuSAJcyygEt2Hl0sJqVzlgpKWwLcYF8oHiPCeM8E0nmBJeV7N5HyvkjiAiBf5m5wjE1yruAqUFUWwQxXC5RbA2J/gUVheFIKqDjPqF0J8ntLIFQAErsoqPUdyqh+zSCaFIMVRB+zTn7PONwyBll4EsBbFkG5eQQAELJLlbZXlWQCIsdulFvK8lfs2T5f5PnTggHK/oCrMX0s0fURwVZ4D8OKcowZ6Tl6zS1v3dues1kEKKJsvZpDMwcK2Z4kAvAsB0AYG6nV5leWECnvACiZcE1jB0CgMV1FBD9hEPUHQnl4D9gsJACI/MegmGkFGC2HAdACQvIOdN5asCVurWKMgEAyTNgChEOIYAHW6MdFvRpY8a4yybvLKGG4WgW2ZVE7KigeX8MrlnIxjtp0b0LmwASVA7JLoCMqsAqrZResWjYySO62kK1ilMhK/j+nwvlKAopATHUn2gU/ZZ6DAxF1vQnP6AMgZrxnW7OdD74ozL6Sy+lb7z7lO7pO5pQGC5zuAafX+qDFH/sUpoto/qO7DCjZdMdFcDaj2rmhvOrTgOYbYAum5HrdHJvXVR+JOcWkQfaXSE0CAqDTJQIlXknpfFOTIsxkyco2Xid5MWGYq6XwydMnBoZGSRmaInvR+KM8vLMkfbB0JKVtPpTqWAfh3U9wBH6keL4G5WNXMQ5dEzPTYUgHqUinqIA7OaAc5e8FSDsPvtw/A+mroPReh/Sgf0VAANsFwLJJA3omhupgC0IVx7LktnIrqnF+qQAABlMBEWFboIisBMuStGoFBA/ZuzFGsgADX7CV5LwqSuUlcoYCAiAQiIBwWGWIUgEhJbKzQEw9Ewx9k1WmJTiwRhuAiDcKwKQFAACFuzWQiCCCIABhAQRbyRsBWLyKgFBHQnZAAAcWKEVlba2Ig4BdGwO7D3VvrGkBEAQfkFDvd209l7/37uA6+1IH7jkRZsHNN2fbCgisA8+89/NCOkdA4h79pGbBEeg9WxcFHEU0d46sAT77WPofFYByCIHqOcfU4x5Dv7bAACy5oAAqCgWfdgiPdhQTjqRUHIFIV7IBijiSS/2ayIUbpsG7E8Xkl3eQKDTeNlLMmg5ka6LG+gWak1rreb7Xk/ts1WH7FPYVHgPClspFQXIVhvCcaaduujvG93ky8MqbleqCqLH7HGrNDu2Abuo1u2O6HZ1MwwTQuhm1lexXWSGpxLCxERt2R4y6vCCgTpo1LVatCxj0OV7Y/Y9iDGbodnqfPseGGpPU9669N8sE4LweX0Plfu3N9wQ0k010ILIcMR33ONJJ6QaZqBiDbvGNdSFV5DjFTUMu5H7pyPScJ/gd3dPsZgaVRO8X3qbfg9RmWAEqmfXPvU3prAJmyrTlc0rFEG2/oPWjD9bMAcv84krBxvMFQEEjA0gLgUhXBLAIAIgOAyB4YyBf988AB+bAAAXgACluw2QAA5AAMndAQI7VP2uy5k0w3CaD7R0EowX1z3D1d03yjxNG9wK373rxyz5ngHxkJjJV33ILDxpioLvWn1ZnZmy2GT5nyR8QmRDy4ynR4IYxoLyW8V4CgGHTbwkNo2XynxkL0VAiUOdz1CVmDHoDsjICrCBWhTMxHSuRAFaEkHZmwXP3oMIHZykC9E8mlUtRt3NgqH7HNHgEkG7CF2wX7Fqx0DNwfzdBLVaBfz6xCA/yOTwG/3oBMGwBEAPUQFm3CBAMgBgJoXgOQNQMwOwMsJDj8O3CVRVTt1lDYDbhIy0P3zFEqMthADV05Wg2E0SnEO0LFEaNS0qwy1TCkGZiDSYVDQz3DVOk4WGOVE6VmRMN6ScxXQq3S2qxzy4ISNKxS3NDSyq16LnmuXk0kxEwsI2J6KRjUwIJ9QS1NGtiWKHx42oKTkfHyxTR9jsmNwDg3HqWjTaJqOHzehXzHzuKDhDj4EqKuISW+Odl+L4011TmBOqIoO4NUNuPHSDkQDwh0BEEXQT2DQTCGJTzYTcTGNxK6ATAYGywGWWSEKLmUBLnrjIJQzhPMCpLri/giyLhEDiCrEpAcQ2WTwuhGI4QpR5KkUKimEvEJBBO4wjz+KRMvQpJbiIx1gDTEL33pL7gVJIxUXFPVjSlH302Tg5S7HJXAkmBmFqkPCsEPAiF4Cakmk/RwhNDExEAk0UxAH1KshOIKAxNXVAMHF7VtTaCIBoCgHbSyAuVlMUCpIoF4AqDKD6MIFaD8jMRjFtD8EQlPQbkjAgH2AUAdKdN4DwEECFmaEwWwAXB2XIi8k1SEF4BzIU14GB1cTT3DMojrOgDTlQDiwswJkT2xKJi1wbNOjIAgJnDLPyBSLwAtijL2l4BYn7PIVHLIHHNTiwHbh7SaJHK8gXInIJN5NnMaA3MXIJnpi7OLHXLHInIQWrKoHFT1lPM3NTgvKaAtgaV3JACIjvMPOdB1wgBdBfIvKwDdTKEzHkMgD5L3LPPvKPMfKF3vPbmrONVAvLPAo/KrKgrGH4B6D4DKAoD5IsSAA=)

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
    "checkver":"github",
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
    ],
    "checkver":{
        "url": "检查链接",
        "regex": "点击下载 程序名([\\d.]+)程序后缀"
    },
    "checkver": {
        "github": "https://github.com/maxmind/geoipupdate"
    }
}
```
