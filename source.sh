#!/bin/bash

mkdir -p ~/.pip
echo -e "\
[global]\ntimeout = 6000\n\
index-url = https://pypi.tuna.tsinghua.edu.cn/simple\n\
trusted-host = http://pypi.tuna.tsinghua.edu.cn" \
> ~/.pip/pip.conf
