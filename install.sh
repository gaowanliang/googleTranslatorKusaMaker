#!/bin/bash

sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' "${PREFIX}/etc/apt/sources.list"
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list
apt update
pkg install python -y
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pkg install git -y
git clone https://gitee.com/gaowanliang/googleTranslatorKusaMaker.git
mv googleTranslatorKusaMaker g
cd g
pip install -r requirements.txt
python main.py