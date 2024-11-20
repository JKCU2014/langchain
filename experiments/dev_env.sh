#!/bin/bash

# brew install python@3.11
# python3.11 -m pip install --upgrade pip
# pip3.11 install virtualenv

python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
poetry config repositories.pypi-mirror https://mirrors.aliyun.com/pypi/simple/
poetry config virtualenvs.in-project true
poetry install --no-interaction --no-ansi --with dev,test,docs
poetry show
