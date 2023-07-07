# aws-crt-python-musllinux

As of `v0.16.21`, the official [awscrt](https://github.com/awslabs/aws-crt-python/) ships musllinux wheels. The `-f` argument to pip can be removed if you install the latest version. This repository will still live in case one needs musllinux wheels of older versions.

~~Currently the official [awscrt](https://github.com/awslabs/aws-crt-python/) doesn't provide binary wheels for musllinux like Alpine, this repository builds musllinux wheels periodically as the awscrt version updated.~~

## Installation

```
pip install awscrt -f https://qqaatw.github.io/aws-crt-python-musllinux/
```
