# The _Cairo smart test suite_

Author: Jamie Gabbay

## What is this?

This repository contains `cairotest`; an automated unit- and property-based test suite for the [Cairo programming language](https://www.cairo-lang.org/) based on [pytest](https://docs.pytest.org/) and [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).

I am pleased to share this with the Cairo community, and feedback and suggestions are welcome.


## How to use Cairo test suite

### Install

Just use `pip` in the usual way.  For example on a Linux environment this should work:
```
pip3 cairotest
```

### Examples

A short tutorial is [`here`](https://github.com/bellissimogiorno/cairotest/tree/main/cairotest-demo).

For more robust usage see the [cairo-integer-types](https://github.com/bellissimogiorno/cairo-integer-types/tree/main/) library.  See any file whose name begins with `test_`, as in [`test_biguint.py`](https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_unbounded/test_bigint.py) or [`test_uint125.py`](https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/test_uint125.py).


### Install Cairo

Presumably if you're interested in `cairotest` then you have Cairo installed, but just in case ...

* [Official Cairo install instructions are here](https://www.cairo-lang.org/docs/quickstart.html#installation) and
* [my personal setup script is below](#my-install)


## Why do we need a Cairo test framework?

Seriously?  You do!

See [this repo](https://github.com/bellissimogiorno/cairo-integer-types/tree/main/) for usage examples.

## My setup

This is what I type to get set up and running with a Cairo development environment on a fresh machine running Debian linux (Ubuntu flavour).  Help yourself (but don't blame me if something goes wrong):

```
# Make sure the ambient Debian OS is up-to-date
sudo apt update
sudo apt upgrade

# Cairo is developed on Python 3.7 so let's get that.
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev libgmp-dev
# Download Python 3.7 and cd into directory
wget https://www.python.org/ftp/python/3.7.13/Python-3.7.13.tgz
tar xvzf Python-3.7.13.tgz
cd Python-3.7.13
# Configure compilation
./configure --enable-optimizations
# Make (8 core system)
make -j 8
# Install
# IMPORTANT: altinstall means we don't overwrite your machine's native version of Python!
sudo make altinstall

# Create Python3.7 virtual environment
python3.7 -m venv ~/cairo_venv-3.7
# Jump into the venv
source ~/cairo_venv-3.7/bin/activate

# Install prerequisites (works for Cairo 0.8)
pip3 install jinja2 pytest pytest-reverse hypothesis cairo-lang black pytest-xdist[psutil]

# Now install cairotest
pip3 install cairotest
```

## Feedback and comments ...

... are very welcome.  Thanks in advance.
