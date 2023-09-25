#!/bin/bash
# sudo ln -s /mnt/c/Windows/Fonts /usr/share/fonts/font
# fc-cache -fv
mkdir -p ~/.pip
echo -e "\
[global]\ntimeout = 6000\n\
index-url = https://pypi.tuna.tsinghua.edu.cn/simple\n\
trusted-host = http://pypi.tuna.tsinghua.edu.cn" \
> ~/.pip/pip.conf
