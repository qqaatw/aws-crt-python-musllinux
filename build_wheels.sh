#!/bin/bash
set -e -u -x

if [ ! -d aws-crt-python ] 
then
    git clone https://github.com/awslabs/aws-crt-python.git --recursive
fi

# Check out and update latest version
cd aws-crt-python/
git checkout $(git tag | sort -V | tail -1)
python ./continuous-delivery/update-version.py

python -m cibuildwheel --output-dir "../wheelhouse"